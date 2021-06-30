#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : responses
Version  : 0.13.3
Release  : 28
URL      : https://files.pythonhosted.org/packages/fe/5e/4a15f6d998e7bb3b6fe774286893784f3507ef4d30a6404b6f56eb20691a/responses-0.13.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/fe/5e/4a15f6d998e7bb3b6fe774286893784f3507ef4d30a6404b6f56eb20691a/responses-0.13.3.tar.gz
Summary  : A utility library for mocking out the `requests` Python library.
Group    : Development/Tools
License  : Apache-2.0
Requires: responses-license = %{version}-%{release}
Requires: responses-python = %{version}-%{release}
Requires: responses-python3 = %{version}-%{release}
Requires: cookies
Requires: mypy
Requires: requests
Requires: six
Requires: urllib3
BuildRequires : Werkzeug
BuildRequires : buildreq-distutils3
BuildRequires : cookies
BuildRequires : coverage
BuildRequires : flake8
BuildRequires : mypy
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-localserver
BuildRequires : python-mock
BuildRequires : requests
BuildRequires : six
BuildRequires : urllib3

%description
=========

%package license
Summary: license components for the responses package.
Group: Default

%description license
license components for the responses package.


%package python
Summary: python components for the responses package.
Group: Default
Requires: responses-python3 = %{version}-%{release}

%description python
python components for the responses package.


%package python3
Summary: python3 components for the responses package.
Group: Default
Requires: python3-core
Provides: pypi(responses)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(urllib3)

%description python3
python3 components for the responses package.


%prep
%setup -q -n responses-0.13.3
cd %{_builddir}/responses-0.13.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625012279
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/responses
cp %{_builddir}/responses-0.13.3/LICENSE %{buildroot}/usr/share/package-licenses/responses/cef33b64c628a8301c7f0a1d2360484b9fe5bed1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/responses/cef33b64c628a8301c7f0a1d2360484b9fe5bed1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
