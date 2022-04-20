#!/bin/bash

cd ~/
curl -I https://github.com/vmraid/vmraid/tree/$TRAVIS_BRANCH | head -n 1 | cut -d $' ' -f2 | (
	read response;
	[ $response == '200' ] && branch=$TRAVIS_BRANCH || branch='develop';
	chair init vmraid-chair --vmraid-path https://github.com/vmraid/vmraid.git --vmraid-branch $branch
)
