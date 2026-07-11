%global tl_name pst-magneticfield
%global tl_revision 69493

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.17a
Release:	%{tl_revision}.1
Summary:	Plotting a magnetic field with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-magneticfield
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-magneticfield.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pst-magneticfield is a PSTricks related package to draw the magnetic
field lines of Helmholtz coils in a two or three dimensional view. There
are several parameters to create a different output. For more
information or some examples read the documentation of the package.

