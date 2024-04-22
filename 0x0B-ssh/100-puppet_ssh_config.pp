# Define SSH client configuration file path
$ssh_config_file = '/home/vagrant/.ssh/config'

# Ensure SSH client configuration file exists
 file { $ssh_config_file:
   ensure => present,
     owner  => 'vagrant',
       group  => 'vagrant',
         mode   => '0600',
         }

         # Ensure SSH client configuration includes private key and disables password authentication
         file_line { 'Declare identity file':
           path    => $ssh_config_file,
             line    => '    IdentityFile ~/.ssh/school',
               match   => '^#?IdentityFile',
                 ensure  => present,
                 }

                 file_line { 'Turn off passwd auth':
                   path    => $ssh_config_file,
                     line    => '    PasswordAuthentication no',
                       match   => '^#?PasswordAuthentication',
                        ensure  => present,
                         }
