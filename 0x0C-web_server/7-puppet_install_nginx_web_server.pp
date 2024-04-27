# setting up nginx using ppupet
exec {'updating apt':
command => 'apt-get update',
path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'installing nginx':
ensure          => installed,
name            => 'nginx',
provider        => 'apt',
install_options => ['-y'],
}

file { 'the home page':
ensure  => file,
path    => '/var/www/html/index.html',
mode    => '0744',
owner   => $::id,
content => "Hello World!\n",
}

file { '/var/www/error':
ensure => directory,
}

file { 'the error page':
ensure  => file,
path    => '/var/www/error/404.html',
mode    => '0744',
owner   => $::id,
content => "Ceci n'est pas une page\n",
}

file { 'setting configuration file':
ensure  => file,
path    => '/etc/nginx/sites-enabled/default',
mode    => '0744',
owner   => 'root',
content =>
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}
	if (\$request_filename ~ redirect_me){
		rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
	error_page 404 /404.html;
	location = /404.html {
		root /var/www/error/;
		internal;
	}
}"
}


exec { 'Start the server':
command => 'service nginx restart',
path    => '/usr/bin:/usr/sbin:/bin'
}
