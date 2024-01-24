# Install flask from pip3

# Ensure python3-pip package is installed
package {'python3-pip':
  ensure => installed
}

# Install Flask using pip3 with the specified version
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}

# Install Werkzeug with the specified version
package {'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip']
}
