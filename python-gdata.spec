Name:           python-gdata
Version:        2.0.18
Release:        1
Summary:        A Python module for accessing online Google services
Group:          Development/Python
License:        ASL 2.0
URL:            http://code.google.com/p/gdata-python-client/
Source0:        http://gdata-python-client.googlecode.com/files/gdata-%{version}.tar.gz
Source1:	python-gdata.rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python >= 2.5

%description
This is a Python module for accessing online Google services, such as:
- Blogger
- Calendar
- Picasa Web Albums
- Spreadsheets
- YouTube
- Notebook

%prep
%setup -q -n gdata-%{version}

chmod -R 755 samples

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt RELEASE_NOTES.txt samples/
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/atom
%{py_puresitedir}/gdata



%changelog
* Sun Apr 22 2012 Götz Waschk <waschk@mandriva.org> 2.0.17-1mdv2012.0
+ Revision: 792676
- new version

* Fri Jan 06 2012 Götz Waschk <waschk@mandriva.org> 2.0.16-1
+ Revision: 758074
- new version

* Wed Oct 19 2011 Götz Waschk <waschk@mandriva.org> 2.0.15-1
+ Revision: 705363
- update to new version 2.0.15

* Tue Mar 08 2011 Götz Waschk <waschk@mandriva.org> 2.0.14-1
+ Revision: 642829
- update to new version 2.0.14

* Thu Nov 18 2010 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdv2011.0
+ Revision: 598751
- update to new version 2.0.13

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 2.0.12-2mdv2011.0
+ Revision: 594297
- rebuild for python 2.7

* Tue Sep 21 2010 Götz Waschk <waschk@mandriva.org> 2.0.12-1mdv2011.0
+ Revision: 580330
- new version

* Tue Aug 03 2010 Götz Waschk <waschk@mandriva.org> 2.0.11-1mdv2011.0
+ Revision: 565469
- new version

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 2.0.10-1mdv2011.0
+ Revision: 550283
- update to new version 2.0.10

* Sat Mar 06 2010 Götz Waschk <waschk@mandriva.org> 2.0.9-1mdv2010.1
+ Revision: 514905
- update to new version 2.0.9

* Sat Feb 27 2010 Götz Waschk <waschk@mandriva.org> 2.0.8-1mdv2010.1
+ Revision: 512386
- update to new version 2.0.8

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 2.0.7-1mdv2010.1
+ Revision: 496953
- update to new version 2.0.7

* Fri Dec 18 2009 Götz Waschk <waschk@mandriva.org> 2.0.6-1mdv2010.1
+ Revision: 479909
- update to new version 2.0.6

* Wed Nov 25 2009 Götz Waschk <waschk@mandriva.org> 2.0.5-1mdv2010.1
+ Revision: 469944
- update to new version 2.0.5

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 2.0.4-1mdv2010.1
+ Revision: 460835
- update to new version 2.0.4

* Sat Aug 22 2009 Götz Waschk <waschk@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 419657
- update to new version 2.0.2

* Fri Jul 24 2009 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 399184
- update to new version 2.0.1

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 390945
- update to new version 2.0.0

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 383897
- update to new version 1.3.3

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 1.3.0-1mdv2010.0
+ Revision: 368982
- new version

* Sat Jan 24 2009 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2009.1
+ Revision: 333236
- update to new version 1.2.4

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.3-2mdv2009.1
+ Revision: 318577
- use newer directory macros
- rebuild for python 2.6

* Sat Dec 06 2008 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdv2009.1
+ Revision: 311214
- update to new version 1.2.3

* Tue Oct 21 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.2-1mdv2009.1
+ Revision: 296328
- new release 1.2.2

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 1.1.1-1mdv2009.0
+ Revision: 250653
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.11-2mdv2009.0
+ Revision: 225130
- rebuild

* Thu Feb 14 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.11-1mdv2008.1
+ Revision: 167718
- new release 1.0.11

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdv2008.1
+ Revision: 160023
- import python-gdata


* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdv2008.1
- initial package based on Fedora spec

* Tue Nov 13 2007 - Bastien Nocera <bnocera@redhat.com> - 1.0.9-1
- Update to 1.0.9

* Sun Oct 21 2007 - Bastien Nocera <bnocera@redhat.com> - 1.0.8-3
- Remove CFLAGS from the make part, as there's no native compilation,
  spotted by Parag AN <panemade@gmail.com>

* Tue Oct 16 2007 - Bastien Nocera <bnocera@redhat.com> - 1.0.8-2
- Remove python-elementtree dep, it's builtin to Python 2.5
- Add samples to the docs, for documentation purposes
- Remove unneeded macro

* Fri Oct 12 2007 - Bastien Nocera <bnocera@redhat.com> - 1.0.8-1
- Initial RPM release
