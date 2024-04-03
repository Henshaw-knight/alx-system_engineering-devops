# Fix the nginx requests limit using puppet file
exec { 'update_ulimit':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  provider => shell,
}

exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['update_ulimit'],
}
