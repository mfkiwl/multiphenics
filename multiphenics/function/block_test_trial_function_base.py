# Copyright (C) 2016-2020 by the multiphenics authors
#
# This file is part of multiphenics.
#
# multiphenics is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# multiphenics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with multiphenics. If not, see <http://www.gnu.org/licenses/>.
#

from multiphenics.function.block_function_space import BlockFunctionSpace

class BlockTestTrialFunction_Base(tuple):
    def __new__(cls, arg1, Generator):
        assert isinstance(arg1, BlockFunctionSpace)
        return tuple.__new__(cls, [Generator(V, block_function_space=arg1, block_index=block_index) for (block_index, V) in enumerate(arg1)])

    def __init__(self, arg1, Generator):
        assert isinstance(arg1, BlockFunctionSpace)
        self._block_function_space = arg1

    def block_function_space(self):
        return self._block_function_space
