# Change the OS configuration so that it is possible to login
# with the holberton user and a file without any error message.
# Fix problem of high amount of files opened
exec { 'hard_nofile':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/g" /etc/security/limits.conf',
  provider => shell
}

exec { 'soft_nofile':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/g" /etc/security/limits.conf',
  provider => shell
}
