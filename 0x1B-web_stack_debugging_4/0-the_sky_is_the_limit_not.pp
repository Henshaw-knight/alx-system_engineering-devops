#!/usr/bin/env bash
# Fix the nginx requests limit using puppet file
exec { 'update_ulimit':
  command  => 'sed -i "s/15/4096" /etc/default/nginx',
  provider => shell
}

exec { 'restart_nginx':
  command  => 'service nginx restart',
  provider => shell,
  require  => Exec['update_ulimit']
}
