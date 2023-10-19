// Import the module
var readdirp = require('readdirp');

var settings = {
    root: '/Users/avirajkhare00/Music',
    entryType: 'all',
    // Filter files with js and json extension
    fileFilter: [ '*.txt' ],
    // Filter by directory
    directoryFilter: [ '!.git', '!*modules' ],
};

// In this example, this variable will store all the paths of the files and directories inside the providen path
var allFilePaths = [];

// Iterate recursively through a folder
readdirp(settings,
    // This callback is executed everytime a file or directory is found inside the providen path
    function(fileInfo) {
        
        // Store the fullPath of the file/directory in our custom array 
        allFilePaths.push(
            fileInfo.fullPath
        );
        //console.log(fileInfo.fullPath);
    }, 

    // This callback is executed once 
    function (err, res) {
        if(err){
            throw err;
        }

        // An array with all the fileEntry objects of the folder 
        // console.log(res);
        console.log(allFilePaths);
        // ["c:/file.txt",""]
    }
);