#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
# Caner Candan <caner@candan.fr>, http://caner.candan.fr
#networkfrom .. import UCG, logging

from .. import Network
from .. import logging

logger = logging.getLogger("ucoin/network/peering")


class Base(Network):
    def __init__(self, server=None, port=None):
        super().__init__(module='network/peering', server=server, port=port)


class Peers(Base):
    """GET peering entries of every node inside the currency network."""

    def __get__(self, **kwargs):
        """creates a generator with one peering entry per iteration."""

        return self.merkle_easy_parser('/peers')

    def __post__(self, **kwargs):
        assert 'entry' in kwargs
        assert 'signature' in kwargs

        return self.requests_post('/peers', **kwargs).json()

class Forward(Base):
    """POST a UCG forward document to this node in order to be sent back incoming transactions."""

    def __post__(self, **kwargs):
        assert 'forward' in kwargs
        assert 'signature' in kwargs

        return self.requests_post('/forward', **kwargs).json()

class Status(Base):
    """POST a UCG status document to this node in order notify of its status."""

    def __post__(self, **kwargs):
        assert 'status' in kwargs
        assert 'signature' in kwargs

        return self.requests_post('/status', **kwargs).json()

from . import peers
