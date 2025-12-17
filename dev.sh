#!/usr/bin/env bash
set -euo pipefail

# Small helper to set up user gem bin in PATH, install bundler/jekyll into
# the user's gem directory (no sudo), run bundle install and start the dev server.
# Usage: bash jekyll-site/dev.sh

cd "$(dirname "$0")"

echo "Ruby: $(ruby -v)"
echo "Gem: $(gem -v)"

GEM_USER_DIR=$(ruby -e 'print Gem.user_dir')
echo "Gem user dir: $GEM_USER_DIR"

export PATH="$GEM_USER_DIR/bin:$PATH"

if ! command -v bundle >/dev/null 2>&1; then
  echo "Installing bundler into user gem dir..."
  gem install bundler --no-document --user-install
fi

RUBY_VER=$(ruby -e 'print RUBY_VERSION')
echo "Detected Ruby version: $RUBY_VER"

# If Ruby < 2.7, install a Rouge gem version that supports older Rubies
ruby_major_minor=$(echo "$RUBY_VER" | awk -F. '{printf "%d.%d", $1, $2}')
if awk 'BEGIN{exit ARGV[1]<2.7}' "$ruby_major_minor" 2>/dev/null; then
  echo "Ruby >= 2.7 detected — installing latest jekyll normally."
  if ! gem list -i jekyll >/dev/null 2>&1; then
    echo "Installing jekyll into user gem dir..."
    gem install jekyll --no-document --user-install
  fi
else
  cat <<'MSG'
Ruby < 2.7 detected — installing modern Jekyll and its dependencies on older Rubies
is fragile. Recommended, reproducible approaches:

1) (Recommended) Install a recent Ruby with rbenv (per-project):
   brew install rbenv ruby-build
   rbenv install 3.2.2
   rbenv local 3.2.2
   gem install bundler
   bundle install
   bundle exec jekyll serve --host 127.0.0.1

2) Alternatively (system-wide via Homebrew):
   brew install ruby
   echo 'export PATH="$(brew --prefix ruby)/bin:$PATH"' >> ~/.zprofile
   source ~/.zprofile
   gem install bundler
   bundle install
   bundle exec jekyll serve --host 127.0.0.1

If you prefer not to upgrade Ruby, be aware you'll need to pin several gems
(`rouge`, `json`, ...) and install build tools (Xcode Command Line Tools).
This is brittle and not recommended.

Exiting now so you can choose one of the recommended options and re-run this script.
MSG
  exit 1
fi

echo "Ensuring PATH includes user gem bin:"
echo "PATH=$PATH"

echo "Running bundle install..."
bundle install

echo "Starting Jekyll dev server (http://127.0.0.1:4000)"
bundle exec jekyll serve --host 127.0.0.1
