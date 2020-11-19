#!/bin/sh

# Push dist directory subtree to gh-pages branch for app deploy
git subtree push --prefix dist origin gh-pages
