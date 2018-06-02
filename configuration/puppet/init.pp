class webserver{ 
  if $::osfamily == 'RedHat' {
    package { 'httpd' :
      ensure => present
    }
  } elseif $::osfamily == 'Debian' {
    package { 'apache2' :
      ensure => present
    }
  } else {
    This is not supported
  }
}
