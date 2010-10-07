# No Copyright (-) 2010 The Ampify Authors. This file is under the
# Public Domain license that can be found in the root LICENSE file.

# ------------------------------------------------------------------------------
# try to figure out if we are inside an interactive shell or not
# ------------------------------------------------------------------------------

test "$PS1" && _INTERACTIVE_SHELL=true;

# ------------------------------------------------------------------------------
# the auto-completer for optcomplete used by the amp runner
# ------------------------------------------------------------------------------

_gitreview_completion() {
	COMPREPLY=( $( \
	COMP_LINE=$COMP_LINE  COMP_POINT=$COMP_POINT \
	COMP_WORDS="${COMP_WORDS[*]}"  COMP_CWORD=$COMP_CWORD \
	OPTPARSE_AUTO_COMPLETE=1 $1 ) )
}

# ------------------------------------------------------------------------------
# set us up the bash completion!
# ------------------------------------------------------------------------------

if [ "x$_INTERACTIVE_SHELL" == "xtrue" ]; then

	# first, turn on the extended globbing and programmable completion
	shopt -s extglob progcomp

	# register completers
	complete -o default -F _gitreview_completion git-review
	complete -o default -F _gitreview_completion git-slave

fi

# ------------------------------------------------------------------------------
# clean up after ourselves
# ------------------------------------------------------------------------------

unset _INTERACTIVE_SHELL
