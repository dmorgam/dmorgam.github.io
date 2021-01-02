#!/bin/sh

# Push dist directory subtree to gh-pages branch for app deploy
cp dist/index.html dist/404.html
git subtree push --prefix dist origin gh-pages
