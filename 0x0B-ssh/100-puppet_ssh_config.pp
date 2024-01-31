# Set up SSH configuration using Puppet
file_line { 'find and use private key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
  ensure => 'present'
}

file_line { 'disable password login':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication',
  ensure => 'present'
}
