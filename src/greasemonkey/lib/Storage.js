/**
 * This script is distributed under the MIT licence.
 * http://en.wikipedia.org/wiki/MIT_License
 * 
 * Copyright (c) 2009 Steven G. Brown
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */


/**
 * @class Provides local storage functionality, which is used to implement {UserPreference}.
 */
Storage = {};

/**
 * @returns {Boolean} true if retrieval of stored data is supported, false otherwise
 */
Storage.canGet = function () {
  try {
    return Boolean(GM_getValue) &&
        GM_getValue('test', 'defaultValue') === 'defaultValue';
  } catch (ex) {
    return false;
  }
};

/**
 * Retrieve a value based on a key.
 * @param key the key
 * @param callback callback function that is provided with the retrieved value
 */
Storage.get = function (key, callback) {
  callback(GM_getValue(key));
};

/**
 * @returns {Boolean} true if modification of stored data is supported, false otherwise
 */
Storage.canSet = function () {
  try {
    return Boolean(GM_setValue);
  } catch (ex) {
    return false;
  }
};

/**
 * Store a value based on a key.
 * @param key the key
 * @param value the value
 */
Storage.set = function (key, value) {
  GM_setValue(key, value);
};
