# Puppet file that helps correct Apache 500 error using strace
exec { 'fix apache error':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  provider => 'shell',
  command  => 'sed -i -e "s/phpp/php/g" /var/www/html/wp-settings.php'
}
