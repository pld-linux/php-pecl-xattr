%define		_modname	xattr
%define		_status		stable

Summary:	%{_modname} - extended attributes
Summary(pl):	%{_modname} - rozszerzone atrybuty
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	1f7b7bd91e636ec3e641bac431a1411a
URL:		http://pecl.php.net/package/xattr/
BuildRequires:	attr-devel
BuildRequires:	libtool
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
This package allows to manipulate extended attributes on filesystems
that support them. Requires libattr from Linux XFS project.

In PECL status of this extension is: %{_status}.

%description -l pl
Ten pakiet umo¿liwia manipulowanie rozszerzonymi atrybutami systemów
plików.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,tests/}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
