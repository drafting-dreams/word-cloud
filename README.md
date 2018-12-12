# word-cloud
My friend asked me for help of building a small online demo to show his word-cloud program. So I did this. You can choose 3 files in it, of course you can change these files as you want in the root dir, but you also need to change some code in the vue file cause the file name is static. Then the server will invoke the python executable file to generate a pic about the text file's content you chose. Yeah, I learned how to run other program in my node code, that's why I remained this repository.

## Project setup
```
npm install
```

### Compiles and minifies for production
```
npm run build
```

### After Build
```
python wd.py _test.txt
```
This is to generate the landing img.

### Run the Server
```
node app.js
```

