%define		php_name	php%{?php_suffix}
%define		modname	xattr
%define		status		stable
Summary:	%{modname} - extended attributes
Summary(pl.UTF-8):	%{modname} - rozszerzone atrybuty
Name:		%{php_name}-pecl-%{modname}
Version:	1.1.0
Release:	5
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	bbfe0649cf71105b7e69342fcfc132df
URL:		http://pecl.php.net/package/xattr/
BuildRequires:	attr-devel
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to manipulate extended attributes on filesystems
that support them. Requires libattr from Linux XFS project.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Ten pakiet umożliwia manipulowanie rozszerzonymi atrybutami systemów
plików.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS tests/
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
