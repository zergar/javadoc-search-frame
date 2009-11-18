"""
This script is distributed under the MIT licence.
http://en.wikipedia.org/wiki/MIT_License

Copyright (c) 2009 Steven G. Brown

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

# Developed with Python v3.0.1

import distutils.dir_util, io, os, shutil, sys


def copyFile(name, fromDir, toDir, transformations=()):
  """
  Copy a single file.
  name: Name of the file.
  fromDir: Directory containing the file, relative to the source directory.
  toDir: Directory to copy this file to, relative to the current directory.
  transformations: Transformations to apply the contents of this file during
                   the copy operation (the original file will be unchanged).
  """

  fromPath = os.path.join(fromDir, name)
  toPath = os.path.join(toDir, name)
  copyAndRenameFile(fromPath, toPath, transformations)


def copyFiles(names, fromDir, toDir, transformations=()):
  """
  Copy multiple files.
  names: Names of the files.
  fromDir: Directory containing the file, relative to the source directory.
  toDir: Directory to copy this file to, relative to the current directory.
  transformations: Transformations to apply the contents of this file during
                   the copy operation (the original file will be unchanged).
  """

  for name in names:
    copyFile(name, fromDir, toDir, transformations)


def copyAndRenameFile(fromPath, toPath, transformations=()):
  """
  Copy and rename a single file.
  fromPath: Path to the file, relative to the source directory.
  toPath: Path to copy this file to, relative to the current directory.
  transformations: Transformations to apply the contents of this file during
                   the copy operation (the original file will be unchanged).
  """

  absFromPath = os.path.abspath(
      os.path.join(sys.path[0], '..', 'src', fromPath))
  absToPath = os.path.abspath(toPath)
  absToPathDir = os.path.dirname(absToPath)
  distutils.dir_util.mkpath(absToPathDir)
  if len(transformations) is 0:
    shutil.copy(absFromPath, absToPathDir)
  else:
    with io.open(absFromPath) as fromFile:
      fileContents = fromFile.read()
    for transformation in transformations:
      fileContents = transformation(fileContents)
    with io.open(absToPath, 'w', newline='\n') as toFile:
      toFile.write(fileContents)