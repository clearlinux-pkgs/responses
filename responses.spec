#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : responses
Version  : 0.10.5
Release  : 7
URL      : https://files.pythonhosted.org/packages/c9/3b/bea0bfc243072a3d910befae4d1fb585276260abcac2a62109e01064c551/responses-0.10.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/c9/3b/bea0bfc243072a3d910befae4d1fb585276260abcac2a62109e01064c551/responses-0.10.5.tar.gz
Summary  : A utility library for mocking out the `requests` Python library.
Group    : Development/Tools
License  : Apache-2.0
Requires: responses-license = %{version}-%{release}
Requires: responses-python = %{version}-%{release}
Requires: responses-python3 = %{version}-%{release}
Requires: cookies
Requires: requests
Requires: six
BuildRequires : Werkzeug
BuildRequires : buildreq-distutils3
BuildRequires : cookies
BuildRequires : coverage
BuildRequires : flake8
BuildRequires : pytest
BuildRequires : pytest-cov
BuildRequires : pytest-localserver
BuildRequires : requests
BuildRequires : six
Patch1: 0001-Fix-testcase-test_assert_all_requests_are_fired-fail.patch

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

%description python3
python3 components for the responses package.


%prep
%setup -q -n responses-0.10.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570664144
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/responses
cp LICENSE %{buildroot}/usr/share/package-licenses/responses/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/responses/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
