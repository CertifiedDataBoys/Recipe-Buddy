// https://bytenota.com/javascript-how-to-store-data-in-html5-session-storage/
var SessionStorageHelper = (function() {

    _isSupported = function() {
        return (typeof(Storage) !== 'undefined');
    };

    // get saved data from sessionStorage
    get = function(key) {
        var value = null;

        if (_isSupported()) {
            var saved = sessionStorage[key];
            if (saved) {
                value = JSON.parse(saved);
            }
        }

        return value;
    };

    // save data to sessionStorage
    save = function(key, value) {
        if (_isSupported()) {
            value = JSON.stringify(value);
            try {
                sessionStorage.setItem(key, value);
            } catch (error) {
                console.log(error);
            }
        }
    };

    // remove saved data from sessionStorage
    remove = function(key) {
        if (_isSupported()) {
            sessionStorage.removeItem(key);
        }
    };

    // remove all saved data from sessionStorage
    clear = function() {
        if (_isSupported()) {
            sessionStorage.clear();
        }
    };

    return {
        get: get,
        save: save,
        remove: remove,
        clear: clear
    };

})();