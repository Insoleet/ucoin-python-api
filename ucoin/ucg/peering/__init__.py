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
#

from .. import UCG

class Base(UCG):
    def __init__(self):
        super().__init__('ucg/peering')

class Keys(Base):
    """GET PGP keys' fingerprint this node manages, i.e. this node will have transactions history and follow ohter nodes for this history."""

    def get(self):
        """creates a generator with one transaction per iteration."""

        return self.merkle_easy_parser('/keys')

class Peer(Base):
    """GET the peering informations of this node."""

    def get(self):
        """returns peering entry of the node."""

        return self.requests_get('/peer').json()

class Peers(Base):
    """GET peering entries of every node inside the currency network."""

    def get(self):
        """creates a generator with one peering entry per iteration."""

        return self.merkle_easy_parser('/peers')

    def post(self):
        pass

class Forward(Base):
    """POST a UCG forward document to this node in order to be sent back incoming transactions."""

    def post(self):
        pass

class Status(Base):
    """POST a UCG status document to this node in order notify of its status."""

    def post(self):
        pass

from . import peers