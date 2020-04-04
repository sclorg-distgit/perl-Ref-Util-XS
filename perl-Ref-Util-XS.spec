%{?scl:%scl_package perl-Ref-Util-XS}

# Run optional tests
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Ref_Util_XS_enables_optional_test
%else
%bcond_with perl_Ref_Util_XS_enables_optional_test
%endif

Name:		%{?scl_prefix}perl-Ref-Util-XS
Version:	0.117
Release:	8%{?dist}
Summary:	Utility functions for checking references
License:	MIT
URL:		https://metacpan.org/release/Ref-Util-XS
Source0:	https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-XS-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl-devel
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module
BuildRequires:	%{?scl_prefix}perl(Exporter) >= 5.57
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(warnings)
BuildRequires:	%{?scl_prefix}perl(XSLoader)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(constant)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.94
%if %{with perl_Ref_Util_XS_enables_optional_test}
# Optional Tests
BuildRequires:	%{?scl_prefix}perl(B::Concise)
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta) >= 2.120900
BuildRequires:	%{?scl_prefix}perl(Readonly)
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

# Avoid provides for private objects
%{?perl_default_filter}

%description
Ref::Util::XS introduces several functions to help identify references in a
faster and smarter way.

%prep
%setup -q -n Ref-Util-XS-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Ref/
%{perl_vendorarch}/Ref/
%{_mandir}/man3/Ref::Util::XS.3*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.117-8
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.117-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.117-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.117-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.117-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.117-3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Paul Howarth <paul@city-fan.org> - 0.117-1
- Update to 0.117
  - Allow the custom OPs to be deparsed with B::Deparse
  - Optimize the shared object size by moving common call checker logic into a
    function

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.116-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.116-3
- Perl 5.26 rebuild

* Tue May 30 2017 Paul Howarth <paul@city-fan.org> - 0.116-2
- Incorporate package review feedback (#1450440)
  - Drop EL6-isms as we need Test::More 0.94, which EL-6 will never have

* Mon May 15 2017 Paul Howarth <paul@city-fan.org> - 0.116-1
- Update to 0.116
  - Changes rephrasing
  - Restore 5.6 compatibility
  - Replace docs with a link to Ref::Util

* Fri May 12 2017 Paul Howarth <paul@city-fan.org> - 0.115-1
- Package renamed Ref-Util-XS to make room for Ref-Util's new pure-Perl
  implementation

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Paul Howarth <paul@city-fan.org> - 0.113-1
- Update to 0.113
  - Fix bugtracker link

* Sun Jan 15 2017 Paul Howarth <paul@city-fan.org> - 0.112-1
- Update to 0.112
  - Fix compilation on Sun (Oracle) and some MSVC compilers (GH#35)

* Fri Dec 30 2016 Paul Howarth <paul@city-fan.org> - 0.111-1
- Update to 0.111
  - Fix test failure on 5.8.5 and under
  - Moved to Dist::Zilla

* Thu Dec 29 2016 Paul Howarth <paul@city-fan.org> - 0.110-1
- Update to 0.110
  - Fix support of 5.8 (GH#29, GH#34)
  - Additional optimizations
  - More extensive test suite

* Mon Aug 29 2016 Paul Howarth <paul@city-fan.org> - 0.101-1
- Update to 0.101
  - A test accidentally added a dependency on Readonly.pm - fixed! (GH#30)
  - Update README

* Sat Aug 27 2016 Paul Howarth <paul@city-fan.org> - 0.100-1
- Update to 0.100
  - Support situations in op-code implementation where the parameters do not
    come as a list
  - Fix memory leak in dangling op
  - Support magic (tied variables)
  - Rework op implementation
  - Speed up by changing the top of the stack instead of POPing and PUSHing
  - Update ppport.h file from Devel::PPPort and remove the copy of SVRXOK since
    it's now available
  - Add license in Pod
  - Specify minimum version of perl (5.6.2)

* Thu Jul 28 2016 Paul Howarth <paul@city-fan.org> - 0.020-2
- Sanitize for Fedora submission

* Thu Jul 28 2016 Paul Howarth <paul@city-fan.org> - 0.020-1
- Initial RPM version
