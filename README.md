![Git-review](https://github.com/tav/git-review/raw/master/review-server/static/logo.png)

Git review is a combined code review, build and testing system built on  
top of Git and GitHub. It was originally developed to help with the  
development of the [Ampify platform], but has since been separated out  
in the hopes of also being useful to other open source projects.

It's made up of 3 separate apps:

* `git-review` — a tool for running automated checks and enabling  
  developers to submit patches very easily.

* `git-slave` — a tool for running automated build slaves.

* `review-server` — a Tornado and App Engine-based web app  
  for managing the code reviews, builds and tests.

**Contribute**

To contribute any patches, simply fork this repository using GitHub and  
send a pull request to me <<http://github.com/tav>>. Thanks!

**Credits**

* [tav], created git-review.

**License**

Everything in this repository, except for the third-party modules in the `lib`
directory, have been released into the [public domain].

—  
Enjoy, tav <<tav@espians.com>>


[Ampify platform]: http://ampify.it
[public domain]: http://ampify.it/unlicense.html

[tav]: http://tav.espians.com
