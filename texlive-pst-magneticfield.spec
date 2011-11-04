# revision 18922
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-magneticfield
# catalog-date 2010-06-12 14:14:46 +0200
# catalog-license lppl
# catalog-version 1.13
Name:		texlive-pst-magneticfield
Version:	1.13
Release:	1
Summary:	Plotting a magnetic field with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-magneticfield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
pst-magneticfield is a PSTricks related package to draw the
magnetic field lines of Helmholtz coils in a two or three
dimensional view. There are several parameters to create a
different output. For more informations or some examples read
the documentation of the package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-magneticfield/pst-magneticfield.pro
%{_texmfdistdir}/tex/generic/pst-magneticfield/pst-magneticfield.tex
%{_texmfdistdir}/tex/latex/pst-magneticfield/pst-magneticfield.sty
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/Changes
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/README
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docEN.pdf
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docEN.tex
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docFR.pdf
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield/pst-magneticfield-docFR.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-magneticfield/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
