Name:           python-gdata
Version:        1.3.0
Release:        %mkrel 1
Summary:        A Python module for accessing online Google services
Group:          Development/Python
License:        ASL 2.0
URL:            http://code.google.com/p/gdata-python-client/
Source0:        http://gdata-python-client.googlecode.com/files/gdata-%{version}.tar.gz
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

chmod 755 samples samples/*
chmod 644 samples/*/*.py

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

