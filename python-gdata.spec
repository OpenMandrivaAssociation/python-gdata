Name:           python-gdata
Version:        2.0.18
Release:        1
Summary:        A Python module for accessing online Google services
Group:          Development/Python
License:        ASL 2.0
URL:            http://code.google.com/p/gdata-python-client/
Source0:        http://gdata-python-client.googlecode.com/files/gdata-%{version}.tar.gz
Source1:	python-gdata.rpmlintrc
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
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
 
%clean

%files
%doc README.txt RELEASE_NOTES.txt samples/
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/atom
%{py_puresitedir}/gdata
