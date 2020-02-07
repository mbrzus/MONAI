# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Compose:
    """
    `Compose` provides the ability to chain a series of calls together in a
    sequence. Each transform in the sequence must take a single argument and
    return a single value, so that the transforms can be called in a chain.

    `Compose` can be used in two ways:
    1. With a series of transforms that accept and return a single ndarray /
    / tensor / tensor-like parameter
    2. With a series of transforms that accept and return a dictionary that
    contains one or more parameters. Such transforms must have pass-through
    semantics; unused values in the dictionary must be copied to the return
    dictionary. It is required that the dictionary is copied between input
    and output of each transform.

    When using the pass-through dictionary operation, you can make use of
    `monai.data.transforms.adaptor` to wrap transforms that don't conform
    to the requirements. This approach allows you to use transforms from
    otherwise incompatible libraries with minimal additional work.
    """
    def __init__(self, transforms=None):
        if transforms is None:
            transforms = []
        if not isinstance(transforms, list):
            raise ValueError("Parameters 'transforms' must be an array")
        self.transforms = transforms

    def __call__(self, input_):
        for transform in self.transforms:
            input_ = transform(input_)
        return input_
