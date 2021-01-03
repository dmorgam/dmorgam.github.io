#!/bin/sh

echo 'Building for production...'
npm run build
cp dist/index.html dist/404.html

#Add files to commit
git add *

#Comitting changes
git commit

# push to remote
git push origin main

# Push dist directory subtree to gh-pages branch for app deploy
git subtree push --prefix dist origin gh-pages
