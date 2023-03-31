Name:		texlive-pst-magneticfield
Version:	63821
Release:	2
Summary:	Plotting a magnetic field with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-magneticfield
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-magneticfield is a PSTricks related package to draw the
magnetic field lines of Helmholtz coils in a two or three
dimensional view. There are several parameters to create a
different output. For more informations or some examples read
the documentation of the package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-magneticfield
%{_texmfdistdir}/tex/generic/pst-magneticfield
%{_texmfdistdir}/tex/latex/pst-magneticfield
%doc %{_texmfdistdir}/doc/generic/pst-magneticfield

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
