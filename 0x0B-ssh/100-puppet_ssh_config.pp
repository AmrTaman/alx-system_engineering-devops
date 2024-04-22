#iam here
include stdlib

file_line {'configuring password auth':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
match  => '#   PasswordAuthentication yes',
line   => '#   PasswordAuthentication no',
}
