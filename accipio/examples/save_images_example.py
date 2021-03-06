
# Copyright 2020 Anders Matre
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example on how to use the save_google_images()."""


import accipio


if __name__ == '__main__':

    # Save images from google to folder
    accipio.images.save_google_images(['snow', 'grass'], path='images', resize=(64, 64))
