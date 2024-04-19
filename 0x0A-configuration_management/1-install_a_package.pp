# iam herer
exec { ' install flask from pip3':
command => '/usr/bin/pip3 install --upgrade flask==2.1.0 werkzeug==2.1.1',
path    => ['/usr/bin', 'usr/local/bin'],
}
