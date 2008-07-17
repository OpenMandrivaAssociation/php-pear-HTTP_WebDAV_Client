%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	%{_pearname} - WebDAV stream wrapper class
Name:		php-pear-%{_pearname}
Version:	0.9.7
Release:	%mkrel 8
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/HTTP_WebDAV_Client/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RFC2518 compliant stream wrapper that allows to use WebDAV server
resources like a regular file system from within PHP.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/{Client,Tools}

install %{_pearname}-%{version}/*.php 		%{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Client/*.php 	%{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Client
install %{_pearname}-%{version}/Tools/*.php 	%{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Tools

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Client
%{_datadir}/pear/%{_class}/%{_subclass}/Tools

%{_datadir}/pear/packages/%{_pearname}.xml


