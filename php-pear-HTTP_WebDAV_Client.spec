%define		_class		HTTP
%define		_subclass	WebDAV
%define		upstream_name	%{_class}_%{_subclass}_Client

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	2
Summary:	WebDAV stream wrapper class
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_WebDAV_Client/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
RFC2518 compliant stream wrapper that allows to use WebDAV server
resources like a regular file system from within PHP.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2012.0
+ Revision: 743485
- 1.0.2

* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3
+ Revision: 742014
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2
+ Revision: 679365
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 594490
- update to new version 1.0.1

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-4mdv2010.1
+ Revision: 477901
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2009.1
+ Revision: 322132
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 278925
- update to new version 1.0.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-8mdv2009.0
+ Revision: 236891
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.9.7-7mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-7mdv2007.0
+ Revision: 81868
- Import php-pear-HTTP_WebDAV_Client

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-1mdk
- initial Mandriva package (PLD import)

