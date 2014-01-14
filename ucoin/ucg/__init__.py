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

from .. import API

class UCG(API):
    def __init__(self, module='ucg'):
        super().__init__(module)

class Pubkey(UCG):
    """GET the public key of the peer."""

    def get(self):
        return self.requests_get('/pubkey').text

class Peering(UCG):
    """GET peering information about a peer."""

    def get(self):
        return self.requests_get('/peering').json()

class THT(UCG):
    """GET/POST THT entries."""

    def __init__(self, pgp_fingerprint=None):
        """
        Use the pgp fingerprint parameter in order to fit the result.

        Arguments:
        - `pgp_fingerprint`: pgp fingerprint to use as a filter
        """

        super().__init__()

        self.pgp_fingerprint = pgp_fingerprint

    def get(self):
        if not self.pgp_fingerprint:
            return self.merkle_easy_parser('/tht').json()

        return self.merkle_easy_parser('/tht/%s' % self.pgp_fingerprint).json()

    def post(self):
        pass

from . import peering