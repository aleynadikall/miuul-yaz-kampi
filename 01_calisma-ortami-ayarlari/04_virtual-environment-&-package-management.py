# UYGULAMA

# Pycharm bize hem python'da çalışmak hem de işletim sistemimizle çalışmak adına alanlar sağlamıştır. Terminal bölümü
# işletim sistemimiz ile konuşmak istediğimiz yani işletim sistemi özelinde yapmak istediğimiz işler için kullandığımız
# bir bölümdür. Burada yazacak olduğumuz komutlar işletim sistemini ilgilendirmektedir. Bir önceki bölümde öğrendiğimiz
# conda ve pip gibi araçlar işletim sistemini ilgilendiren araçlardır. Öncelikle işletim sistemi seviyesinde bir izolasyon
# bir sanallaştırma yapacağız ki onun içerisinde python versiyon ya da versiyonlarını ya da diğer paketleri yükleyip
# kullanmış olacağız. Dolayısıyla şu anda yazacak olduğumuz kodları işletim sistemi ile kullanıyor olacağız. Kodları yorum
# satırı içerisinde vereceğim:
# Sanal ortamların listelenmesi için: conda env list
# Bu komut ile çıkan sonuçta bulunduğumuz sanal ortam yıldızlı şekilde gösterilecektir.

# Sanal ortam oluşturma: conda create -n myenv (myenv yerine başka isimlendirmeler de yapılabilir)

# Oluşturulan sanal ortamı aktif etmek için: conda activate myenv

# Deaktive etmek istersek: conda deactivate

# Yüklü paketlerin listelenmesi: cyonda list

# Bir sanal ortama paket yüklemek istediğimizde: conda install kullanırız. Mesela conda install numpy yazalım.

# Aynı anda birden fazla paket yüklemek istersek: conda install pandas scipy

# Diyelim ki bir proje için özel olarak belirli bir numpy versiyonunu kullanmak istiyoruz öncelikler bir paket silelim
# bunu bu şekilde görelim: conda remove package_name
# numpy'ın 1.20.1 versiyonunu kurmak istiyoruz bunun için conda install numpy =1.20.1 deriz pip'de ise pip install numpy==1.20.1
# deriz. Yani iki eşittir kullanılır. Bu kısım önemli.

# Tekrar conda list ile yüklü olan paketleri görelim.
# Tekrar numpy'ın son versiyonuyla çalışmaya devam etmek istersem ya az önceki işlemleri tekrarlayacağım ya da upgrade
# ifadesi kullanacağım
# Paket yükseltmesi: conda upgrade numpy

# Tüm paketlerin yükseltilmesi için: conda upgrade -all

# pip kullanarak devam edelim.
# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme: pip install pandas

# Paket yükleme versiyona göre: pip install pandas==1.2.1

# conda list ile gözlemlediğimiz paketleri bir çalışma arkadaşımıza atmak istediğimizi düşünelim bunu aktarmanın yolu yaml
# file oluşturmaktır: conda env export > environment.yaml(.yml) pip kullandığımızda ise pip env export > requirement.txt yazmalıyız.
# dosyaları listemlem adına ls komutunu kullanıyoruz.

####
# Windows PowerShell
#
# Try the new cross-platform PowerShell https://aka.ms/pscore6
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# #
# base                  *  C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# #
# base                  *  C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda create -n my_aleyna
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
#
# ==> WARNING: A newer version of conda exists. <==
#   current version: 4.10.3
#   latest version: 4.13.0
#
# Please update conda by running
#
#     $ conda update -n base -c defaults conda
#
#
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3\envs\my_aleyna
#
#
#
# Proceed ([y]/n)? y
#
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# #
# #     $ conda activate my_aleyna
# #
# # To deactivate an active environment, use
# #
# #     $ conda deactivate
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda activate my_aleyna
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda list
# # packages in environment at C:\Users\aleyy\anaconda3:
# #
# # Name                    Version                   Build  Channel
# _ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
# alabaster                 0.7.12             pyhd3eb1b0_0
# anaconda                  2021.11                  py39_0
# anaconda-client           1.9.0            py39haa95532_0
# anaconda-navigator        2.1.1                    py39_0
# anaconda-project          0.10.1             pyhd3eb1b0_0
# anyio                     2.2.0            py39haa95532_2
# appdirs                   1.4.4              pyhd3eb1b0_0
# argh                      0.26.2           py39haa95532_0
# argon2-cffi               20.1.0           py39h2bbff1b_1
# arrow                     0.13.1           py39haa95532_0
# asn1crypto                1.4.0                      py_0
# astroid                   2.6.6            py39haa95532_0
# astropy                   4.3.1            py39hc7d831d_0
# async_generator           1.10               pyhd3eb1b0_0
# atomicwrites              1.4.0                      py_0
# attrs                     21.2.0             pyhd3eb1b0_0
# autopep8                  1.5.7              pyhd3eb1b0_0
# babel                     2.9.1              pyhd3eb1b0_0
# backcall                  0.2.0              pyhd3eb1b0_0
# backports                 1.0                pyhd3eb1b0_2
# backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
# backports.shutil_get_terminal_size 1.0.0              pyhd3eb1b0_3
# backports.tempfile        1.0                pyhd3eb1b0_1
# backports.weakref         1.0.post1                  py_1
# bcrypt                    3.2.0            py39h196d8e1_0
# beautifulsoup4            4.10.0             pyh06a4308_0
# binaryornot               0.4.4              pyhd3eb1b0_1
# bitarray                  2.3.0            py39h2bbff1b_1
# bkcharts                  0.2              py39haa95532_0
# black                     19.10b0                    py_0
# blas                      1.0                         mkl
# bleach                    4.0.0              pyhd3eb1b0_0
# blosc                     1.21.0               h19a0ad4_0
# bokeh                     2.4.1            py39haa95532_0
# boto                      2.49.0           py39haa95532_0
# bottleneck                1.3.2            py39h7cc1a96_1
# brotli                    1.0.9                ha925a31_2
# brotlipy                  0.7.0           py39h2bbff1b_1003
# bzip2                     1.0.8                he774522_0
# ca-certificates           2021.10.26           haa95532_2
# cached-property           1.5.2                      py_0
# certifi                   2021.10.8        py39haa95532_0
# cffi                      1.14.6           py39h2bbff1b_0
# cfitsio                   3.470                he774522_6
# chardet                   4.0.0           py39haa95532_1003
# charls                    2.2.0                h6c2663c_0
# charset-normalizer        2.0.4              pyhd3eb1b0_0
# click                     8.0.3              pyhd3eb1b0_0
# cloudpickle               2.0.0              pyhd3eb1b0_0
# clyent                    1.2.2            py39haa95532_1
# colorama                  0.4.4              pyhd3eb1b0_0
# comtypes                  1.1.10          py39haa95532_1002
# conda                     4.10.3           py39haa95532_0
# conda-build               3.21.6           py39haa95532_0
# conda-content-trust       0.1.1              pyhd3eb1b0_0
# conda-env                 2.6.0                         1
# conda-pack                0.6.0              pyhd3eb1b0_0
# conda-package-handling    1.7.3            py39h8cc25b3_1
# conda-repo-cli            1.0.4              pyhd3eb1b0_0
# conda-token               0.3.0              pyhd3eb1b0_0
# conda-verify              3.4.2                      py_1
# console_shortcut          0.1.1                         4
# contextlib2               0.6.0.post1        pyhd3eb1b0_0
# cookiecutter              1.7.2              pyhd3eb1b0_0
# cryptography              3.4.8            py39h71e12ea_0
# curl                      7.78.0               h86230a5_0
# cycler                    0.10.0           py39haa95532_0
# cython                    0.29.24          py39h604cdb4_0
# cytoolz                   0.11.0           py39h2bbff1b_0
# daal4py                   2021.3.0         py39h757b272_0
# dal                       2021.3.0           haa95532_564
# dask                      2021.10.0          pyhd3eb1b0_0
# dask-core                 2021.10.0          pyhd3eb1b0_0
# dataclasses               0.8                pyh6d0b6a4_7
# debugpy                   1.4.1            py39hd77b12b_0
# decorator                 5.1.0              pyhd3eb1b0_0
# defusedxml                0.7.1              pyhd3eb1b0_0
# diff-match-patch          20200713           pyhd3eb1b0_0
# distributed               2021.10.0        py39haa95532_0
# docutils                  0.17.1           py39haa95532_1
# entrypoints               0.3              py39haa95532_0
# et_xmlfile                1.1.0            py39haa95532_0
# fastcache                 1.1.0            py39h196d8e1_0
# filelock                  3.3.1              pyhd3eb1b0_1
# flake8                    3.9.2              pyhd3eb1b0_0
# flask                     1.1.2              pyhd3eb1b0_0
# fonttools                 4.25.0             pyhd3eb1b0_0
# freetype                  2.10.4               hd328e21_0
# fsspec                    2021.10.1          pyhd3eb1b0_0
# future                    0.18.2           py39haa95532_1
# get_terminal_size         1.0.0                h38e98db_0
# gevent                    21.8.0           py39h2bbff1b_1
# giflib                    5.2.1                h62dcd97_0
# glob2                     0.7                pyhd3eb1b0_0
# greenlet                  1.1.1            py39hd77b12b_0
# h5py                      3.2.1            py39h3de5c98_0
# hdf5                      1.10.6               h7ebc959_0
# heapdict                  1.0.1              pyhd3eb1b0_0
# html5lib                  1.1                pyhd3eb1b0_0
# icc_rt                    2019.0.0             h0cc432a_1
# icu                       58.2                 ha925a31_3
# idna                      3.2                pyhd3eb1b0_0
# imagecodecs               2021.8.26        py39ha1f97ea_0
# imageio                   2.9.0              pyhd3eb1b0_0
# imagesize                 1.2.0              pyhd3eb1b0_0
# importlib-metadata        4.8.1            py39haa95532_0
# importlib_metadata        4.8.1                hd3eb1b0_0
# inflection                0.5.1            py39haa95532_0
# iniconfig                 1.1.1              pyhd3eb1b0_0
# intel-openmp              2021.4.0          haa95532_3556
# intervaltree              3.1.0              pyhd3eb1b0_0
# ipykernel                 6.4.1            py39haa95532_1
# ipython                   7.29.0           py39hd4e2768_0
# ipython_genutils          0.2.0              pyhd3eb1b0_1
# ipywidgets                7.6.5              pyhd3eb1b0_1
# isort                     5.9.3              pyhd3eb1b0_0
# itsdangerous              2.0.1              pyhd3eb1b0_0
# jdcal                     1.4.1              pyhd3eb1b0_0
# jedi                      0.18.0           py39haa95532_1
# jinja2                    2.11.3             pyhd3eb1b0_0
# jinja2-time               0.2.0              pyhd3eb1b0_2
# joblib                    1.1.0              pyhd3eb1b0_0
# jpeg                      9d                   h2bbff1b_0
# json5                     0.9.6              pyhd3eb1b0_0
# jsonschema                3.2.0              pyhd3eb1b0_2
# jupyter                   1.0.0            py39haa95532_7
# jupyter_client            6.1.12             pyhd3eb1b0_0
# jupyter_console           6.4.0              pyhd3eb1b0_0
# jupyter_core              4.8.1            py39haa95532_0
# jupyter_server            1.4.1            py39haa95532_0
# jupyterlab                3.2.1              pyhd3eb1b0_1
# jupyterlab_pygments       0.1.2                      py_0
# jupyterlab_server         2.8.2              pyhd3eb1b0_0
# jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
# keyring                   23.1.0           py39haa95532_0
# kiwisolver                1.3.1            py39hd77b12b_0
# krb5                      1.19.2               h5b6d351_0
# lazy-object-proxy         1.6.0            py39h2bbff1b_0
# lcms2                     2.12                 h83e58a3_0
# lerc                      3.0                  hd77b12b_0
# libaec                    1.0.4                h33f27b4_1
# libarchive                3.4.2                h5e25573_0
# libcurl                   7.78.0               h86230a5_0
# libdeflate                1.8                  h2bbff1b_5
# libiconv                  1.15                 h1df5818_7
# liblief                   0.10.1               hd77b12b_1
# libpng                    1.6.37               h2a8f88b_0
# libspatialindex           1.9.3                h6c2663c_0
# libssh2                   1.9.0                h7a1dbc1_1
# libtiff                   4.2.0                hd0e1b90_0
# libwebp                   1.2.0                h2bbff1b_0
# libxml2                   2.9.12               h0ad7f3c_0
# libxslt                   1.1.34               he774522_0
# libzopfli                 1.0.3                ha925a31_0
# llvmlite                  0.37.0           py39h23ce68f_1
# locket                    0.2.1            py39haa95532_1
# lxml                      4.6.3            py39h9b66d53_0
# lz4-c                     1.9.3                h2bbff1b_1
# lzo                       2.10                 he774522_2
# m2w64-gcc-libgfortran     5.3.0                         6
# m2w64-gcc-libs            5.3.0                         7
# m2w64-gcc-libs-core       5.3.0                         7
# m2w64-gmp                 6.1.0                         2
# m2w64-libwinpthread-git   5.0.0.4634.697f757               2
# markupsafe                1.1.1            py39h2bbff1b_0
# matplotlib                3.4.3            py39haa95532_0
# matplotlib-base           3.4.3            py39h49ac443_0
# matplotlib-inline         0.1.2              pyhd3eb1b0_2
# mccabe                    0.6.1            py39haa95532_1
# menuinst                  1.4.18           py39h59b6b97_0
# mistune                   0.8.4           py39h2bbff1b_1000
# mkl                       2021.4.0           haa95532_640
# mkl-service               2.4.0            py39h2bbff1b_0
# mkl_fft                   1.3.1            py39h277e83a_0
# mkl_random                1.2.2            py39hf11a4ad_0
# mock                      4.0.3              pyhd3eb1b0_0
# more-itertools            8.10.0             pyhd3eb1b0_0
# mpmath                    1.2.1            py39haa95532_0
# msgpack-python            1.0.2            py39h59b6b97_1
# msys2-conda-epoch         20160418                      1
# multipledispatch          0.6.0            py39haa95532_0
# munkres                   1.1.4                      py_0
# mypy_extensions           0.4.3            py39haa95532_0
# navigator-updater         0.2.1            py39haa95532_0
# nbclassic                 0.2.6              pyhd3eb1b0_0
# nbclient                  0.5.3              pyhd3eb1b0_0
# nbconvert                 6.1.0            py39haa95532_0
# nbformat                  5.1.3              pyhd3eb1b0_0
# nest-asyncio              1.5.1              pyhd3eb1b0_0
# networkx                  2.6.3              pyhd3eb1b0_0
# nltk                      3.6.5              pyhd3eb1b0_0
# nose                      1.3.7           pyhd3eb1b0_1006
# notebook                  6.4.5            py39haa95532_0
# numba                     0.54.1           py39hf11a4ad_0
# numexpr                   2.7.3            py39hb80d3ca_1
# numpy                     1.20.3           py39ha4e8547_0
# numpy-base                1.20.3           py39hc2deb75_0
# numpydoc                  1.1.0              pyhd3eb1b0_1
# olefile                   0.46               pyhd3eb1b0_0
# openjpeg                  2.4.0                h4fc8c34_0
# openpyxl                  3.0.9              pyhd3eb1b0_0
# openssl                   1.1.1l               h2bbff1b_0
# packaging                 21.0               pyhd3eb1b0_0
# pandas                    1.3.4            py39h6214cd6_0
# pandocfilters             1.4.3            py39haa95532_1
# paramiko                  2.7.2                      py_0
# parso                     0.8.2              pyhd3eb1b0_0
# partd                     1.2.0              pyhd3eb1b0_0
# path                      16.0.0           py39haa95532_0
# path.py                   12.5.0               hd3eb1b0_0
# pathlib2                  2.3.6            py39haa95532_2
# pathspec                  0.7.0                      py_0
# patsy                     0.5.2            py39haa95532_0
# pep8                      1.7.1            py39haa95532_0
# pexpect                   4.8.0              pyhd3eb1b0_3
# pickleshare               0.7.5           pyhd3eb1b0_1003
# pillow                    8.4.0            py39hd45dc43_0
# pip                       21.2.4           py39haa95532_0
# pkginfo                   1.7.1            py39haa95532_0
# pluggy                    0.13.1           py39haa95532_0
# ply                       3.11             py39haa95532_0
# powershell_shortcut       0.0.1                         3
# poyo                      0.5.0              pyhd3eb1b0_0
# prometheus_client         0.11.0             pyhd3eb1b0_0
# prompt-toolkit            3.0.20             pyhd3eb1b0_0
# prompt_toolkit            3.0.20               hd3eb1b0_0
# psutil                    5.8.0            py39h2bbff1b_1
# ptyprocess                0.7.0              pyhd3eb1b0_2
# py                        1.10.0             pyhd3eb1b0_0
# py-lief                   0.10.1           py39hd77b12b_1
# pycodestyle               2.7.0              pyhd3eb1b0_0
# pycosat                   0.6.3            py39h2bbff1b_0
# pycparser                 2.20                       py_2
# pycurl                    7.44.1           py39hcd4344a_1
# pydocstyle                6.1.1              pyhd3eb1b0_0
# pyerfa                    2.0.0            py39h2bbff1b_0
# pyflakes                  2.3.1              pyhd3eb1b0_0
# pygments                  2.10.0             pyhd3eb1b0_0
# pyjwt                     2.1.0            py39haa95532_0
# pylint                    2.9.6            py39haa95532_1
# pyls-spyder               0.4.0              pyhd3eb1b0_0
# pynacl                    1.4.0            py39hbd8134f_1
# pyodbc                    4.0.31           py39hd77b12b_0
# pyopenssl                 21.0.0             pyhd3eb1b0_1
# pyparsing                 3.0.4              pyhd3eb1b0_0
# pyqt                      5.9.2            py39hd77b12b_6
# pyreadline                2.1              py39haa95532_1
# pyrsistent                0.18.0           py39h196d8e1_0
# pysocks                   1.7.1            py39haa95532_0
# pytables                  3.6.1            py39h56d22b6_1
# pytest                    6.2.4            py39haa95532_2
# python                    3.9.7                h6244533_1
# python-dateutil           2.8.2              pyhd3eb1b0_0
# python-libarchive-c       2.9                pyhd3eb1b0_1
# python-lsp-black          1.0.0              pyhd3eb1b0_0
# python-lsp-jsonrpc        1.0.0              pyhd3eb1b0_0
# python-lsp-server         1.2.4              pyhd3eb1b0_0
# python-slugify            5.0.2              pyhd3eb1b0_0
# pytz                      2021.3             pyhd3eb1b0_0
# pywavelets                1.1.1            py39h080aedc_4
# pywin32                   228              py39he774522_0
# pywin32-ctypes            0.2.0           py39haa95532_1000
# pywinpty                  0.5.7            py39haa95532_0
# pyyaml                    6.0              py39h2bbff1b_1
# pyzmq                     22.2.1           py39hd77b12b_1
# qdarkstyle                3.0.2              pyhd3eb1b0_0
# qstylizer                 0.1.10             pyhd3eb1b0_0
# qt                        5.9.7            vc14h73c81de_0
# qtawesome                 1.0.2              pyhd3eb1b0_0
# qtconsole                 5.1.1              pyhd3eb1b0_0
# qtpy                      1.10.0             pyhd3eb1b0_0
# regex                     2021.8.3         py39h2bbff1b_0
# requests                  2.26.0             pyhd3eb1b0_0
# rope                      0.19.0             pyhd3eb1b0_0
# rtree                     0.9.7            py39h2eaa2aa_1
# ruamel_yaml               0.15.100         py39h2bbff1b_0
# scikit-image              0.18.3           py39hf11a4ad_0
# scikit-learn              0.24.2           py39hf11a4ad_1
# scikit-learn-intelex      2021.3.0         py39haa95532_0
# scipy                     1.7.1            py39hbe87c03_2
# seaborn                   0.11.2             pyhd3eb1b0_0
# send2trash                1.8.0              pyhd3eb1b0_1
# setuptools                58.0.4           py39haa95532_0
# simplegeneric             0.8.1            py39haa95532_2
# singledispatch            3.7.0           pyhd3eb1b0_1001
# sip                       4.19.13          py39hd77b12b_0
# six                       1.16.0             pyhd3eb1b0_0
# snappy                    1.1.8                h33f27b4_0
# sniffio                   1.2.0            py39haa95532_1
# snowballstemmer           2.1.0              pyhd3eb1b0_0
# sortedcollections         2.1.0              pyhd3eb1b0_0
# sortedcontainers          2.4.0              pyhd3eb1b0_0
# soupsieve                 2.2.1              pyhd3eb1b0_0
# sphinx                    4.2.0              pyhd3eb1b0_1
# sphinxcontrib             1.0              py39haa95532_1
# sphinxcontrib-applehelp   1.0.2              pyhd3eb1b0_0
# sphinxcontrib-devhelp     1.0.2              pyhd3eb1b0_0
# sphinxcontrib-htmlhelp    2.0.0              pyhd3eb1b0_0
# sphinxcontrib-jsmath      1.0.1              pyhd3eb1b0_0
# sphinxcontrib-qthelp      1.0.3              pyhd3eb1b0_0
# sphinxcontrib-serializinghtml 1.1.5              pyhd3eb1b0_0
# sphinxcontrib-websupport  1.2.4                      py_0
# spyder                    5.1.5            py39haa95532_1
# spyder-kernels            2.1.3            py39haa95532_0
# sqlalchemy                1.4.22           py39h2bbff1b_0
# sqlite                    3.36.0               h2bbff1b_0
# statsmodels               0.12.2           py39h2bbff1b_0
# sympy                     1.9              py39haa95532_0
# tbb                       2021.4.0             h59b6b97_0
# tbb4py                    2021.4.0         py39h59b6b97_0
# tblib                     1.7.0              pyhd3eb1b0_0
# terminado                 0.9.4            py39haa95532_0
# testpath                  0.5.0              pyhd3eb1b0_0
# text-unidecode            1.3                pyhd3eb1b0_0
# textdistance              4.2.1              pyhd3eb1b0_0
# threadpoolctl             2.2.0              pyh0d69192_0
# three-merge               0.1.1              pyhd3eb1b0_0
# tifffile                  2021.7.2           pyhd3eb1b0_2
# tinycss                   0.4             pyhd3eb1b0_1002
# tk                        8.6.11               h2bbff1b_0
# toml                      0.10.2             pyhd3eb1b0_0
# toolz                     0.11.1             pyhd3eb1b0_0
# tornado                   6.1              py39h2bbff1b_0
# tqdm                      4.62.3             pyhd3eb1b0_1
# traitlets                 5.1.0              pyhd3eb1b0_0
# typed-ast                 1.4.3            py39h2bbff1b_1
# typing_extensions         3.10.0.2           pyh06a4308_0
# tzdata                    2021e                hda174b7_0
# ujson                     4.0.2            py39hd77b12b_0
# unicodecsv                0.14.1           py39haa95532_0
# unidecode                 1.2.0              pyhd3eb1b0_0
# urllib3                   1.26.7             pyhd3eb1b0_0
# vc                        14.2                 h21ff451_1
# vs2015_runtime            14.27.29016          h5e58377_2
# watchdog                  2.1.3            py39haa95532_0
# wcwidth                   0.2.5              pyhd3eb1b0_0
# webencodings              0.5.1            py39haa95532_1
# werkzeug                  2.0.2              pyhd3eb1b0_0
# wheel                     0.37.0             pyhd3eb1b0_1
# whichcraft                0.6.1              pyhd3eb1b0_0
# widgetsnbextension        3.5.1            py39haa95532_0
# win_inet_pton             1.1.0            py39haa95532_0
# win_unicode_console       0.5              py39haa95532_0
# wincertstore              0.2              py39haa95532_2
# winpty                    0.4.3                         4
# wrapt                     1.12.1           py39h196d8e1_1
# xlrd                      2.0.1              pyhd3eb1b0_0
# xlsxwriter                3.0.1              pyhd3eb1b0_0
# xlwings                   0.24.9           py39haa95532_0
# xlwt                      1.3.0            py39haa95532_0
# xmltodict                 0.12.0             pyhd3eb1b0_0
# xz                        5.2.5                h62dcd97_0
# yaml                      0.2.5                he774522_0
# zfp                       0.5.5                hd77b12b_6
# zict                      2.0.0              pyhd3eb1b0_0
# zipp                      3.6.0              pyhd3eb1b0_0
# zlib                      1.2.11               h62dcd97_4
# zope                      1.0              py39haa95532_1
# zope.event                4.5.0            py39haa95532_0
# zope.interface            5.4.0            py39h2bbff1b_0
# zstd                      1.4.9                h19a0ad4_0
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda update -n base -c defaults conda
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3
#
#   added / updated specs:
#     - conda
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     conda-4.13.0               |   py39haa95532_0         923 KB
#     conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
#     ------------------------------------------------------------
#                                            Total:         1.6 MB
#
# The following packages will be UPDATED:
#
#   conda                               4.10.3-py39haa95532_0 --> 4.13.0-py39haa95532_0
#   conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0
#
#
#
#
# Downloading and Extracting Packages
# conda-4.13.0         | 923 KB    | ########################################## | 100%
# conda-package-handli | 729 KB    | ########################################## | 100%
# Verifying transaction: done
# Executing transaction: done
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda install numpy
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
# # All requested packages already installed.
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda install pandas scipy
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
# # All requested packages already installed.
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda remove numpy
# Collecting package metadata (repodata.json): done
# Solving environment: done
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3
#
#   removed specs:
#     - numpy
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     anaconda-client-1.10.0     |   py39haa95532_0         166 KB
#     anyio-3.5.0                |   py39haa95532_0         167 KB
#     argon2-cffi-21.3.0         |     pyhd3eb1b0_0          15 KB
#     argon2-cffi-bindings-21.2.0|   py39h2bbff1b_0          36 KB
#     asttokens-2.0.5            |     pyhd3eb1b0_0          20 KB
#     attrs-21.4.0               |     pyhd3eb1b0_0          51 KB
#     backports-1.1              |     pyhd3eb1b0_0           4 KB
#     beautifulsoup4-4.11.1      |   py39haa95532_0         190 KB
#     bleach-4.1.0               |     pyhd3eb1b0_0         123 KB
#     ca-certificates-2022.4.26  |       haa95532_0         124 KB
#     certifi-2022.6.15          |   py39haa95532_0         153 KB
#     cffi-1.15.0                |   py39h2bbff1b_1         224 KB
#     click-8.0.4                |   py39haa95532_0         155 KB
#     conda-build-3.21.9         |   py39haa95532_0         555 KB
#     debugpy-1.5.1              |   py39hd77b12b_0         2.6 MB
#     decorator-5.1.1            |     pyhd3eb1b0_0          12 KB
#     entrypoints-0.4            |   py39haa95532_0          17 KB
#     executing-0.8.3            |     pyhd3eb1b0_0          18 KB
#     filelock-3.6.0             |     pyhd3eb1b0_0          12 KB
#     idna-3.3                   |     pyhd3eb1b0_0          49 KB
#     ipykernel-6.9.1            |   py39haa95532_0         200 KB
#     ipython-8.3.0              |   py39haa95532_0        1010 KB
#     jedi-0.18.1                |   py39haa95532_1         982 KB
#     jpeg-9e                    |       h2bbff1b_0         292 KB
#     jsonschema-4.4.0           |   py39haa95532_0         139 KB
#     jupyter_client-7.2.2       |   py39haa95532_0         216 KB
#     jupyter_core-4.10.0        |   py39haa95532_0          96 KB
#     jupyter_server-1.17.1      |   py39haa95532_0         374 KB
#     jupyterlab-3.3.2           |     pyhd3eb1b0_0         3.6 MB
#     jupyterlab_server-2.10.3   |     pyhd3eb1b0_1          48 KB
#     libarchive-3.5.2           |       h214662b_0         781 KB
#     libiconv-1.16              |       h2bbff1b_2         651 KB
#     liblief-0.11.5             |       hd77b12b_1         2.1 MB
#     libtiff-4.2.0              |       he0120a3_1         754 KB
#     libwebp-1.2.2              |       h2bbff1b_0         658 KB
#     libxml2-2.9.14             |       h0ad7f3c_0         1.5 MB
#     markupsafe-2.0.1           |   py39h2bbff1b_0          24 KB
#     nbclassic-0.3.5            |     pyhd3eb1b0_0          22 KB
#     nbclient-0.5.13            |   py39haa95532_0         108 KB
#     nbconvert-6.4.4            |   py39haa95532_0         517 KB
#     nbformat-5.3.0             |   py39haa95532_0         146 KB
#     nest-asyncio-1.5.5         |   py39haa95532_0          16 KB
#     notebook-6.4.11            |   py39haa95532_0         4.5 MB
#     openssl-1.1.1p             |       h2bbff1b_0         4.8 MB
#     packaging-21.3             |     pyhd3eb1b0_0          36 KB
#     pandocfilters-1.5.0        |     pyhd3eb1b0_0          11 KB
#     parso-0.8.3                |     pyhd3eb1b0_0          70 KB
#     pillow-9.0.1               |   py39hdc2b20a_0         921 KB
#     pkginfo-1.8.2              |     pyhd3eb1b0_0          27 KB
#     prometheus_client-0.13.1   |     pyhd3eb1b0_0          47 KB
#     psutil-5.9.0               |   py39h2bbff1b_0         349 KB
#     pure_eval-0.2.2            |     pyhd3eb1b0_0          14 KB
#     py-lief-0.11.5             |   py39hd77b12b_1         1.7 MB
#     pycparser-2.21             |     pyhd3eb1b0_0          94 KB
#     pygments-2.11.2            |     pyhd3eb1b0_0         759 KB
#     python-fastjsonschema-2.15.1|     pyhd3eb1b0_0          29 KB
#     pytz-2022.1                |   py39haa95532_0         195 KB
#     pywin32-302                |   py39h2bbff1b_2         5.6 MB
#     pywinpty-2.0.2             |   py39h5da7b33_0         200 KB
#     pyzmq-22.3.0               |   py39hd77b12b_2         632 KB
#     qtpy-2.0.1                 |     pyhd3eb1b0_0          40 KB
#     requests-2.28.0            |   py39haa95532_0         100 KB
#     setuptools-61.2.0          |   py39haa95532_0         1.0 MB
#     six-1.16.0                 |     pyhd3eb1b0_1          18 KB
#     soupsieve-2.3.1            |     pyhd3eb1b0_0          34 KB
#     sqlite-3.38.5              |       h2bbff1b_0         798 KB
#     stack_data-0.2.0           |     pyhd3eb1b0_0          22 KB
#     terminado-0.13.1           |   py39haa95532_0          31 KB
#     testpath-0.6.0             |   py39haa95532_0          85 KB
#     tk-8.6.12                  |       h2bbff1b_0         3.1 MB
#     tqdm-4.64.0                |   py39haa95532_0         155 KB
#     traitlets-5.1.1            |     pyhd3eb1b0_0          84 KB
#     typing-extensions-4.1.1    |       hd3eb1b0_0           8 KB
#     typing_extensions-4.1.1    |     pyh06a4308_0          28 KB
#     tzdata-2022a               |       hda174b7_0         109 KB
#     ujson-5.1.0                |   py39hd77b12b_0          50 KB
#     urllib3-1.26.9             |   py39haa95532_0         190 KB
#     websocket-client-0.58.0    |   py39haa95532_4          69 KB
#     wheel-0.37.1               |     pyhd3eb1b0_0          33 KB
#     widgetsnbextension-3.5.2   |   py39haa95532_0         646 KB
#     xz-5.2.5                   |       h8cc25b3_1         246 KB
#     zlib-1.2.12                |       h8cc25b3_2         116 KB
#     zstd-1.5.2                 |       h19a0ad4_0         509 KB
#     ------------------------------------------------------------
#                                            Total:        46.2 MB
#
# The following NEW packages will be INSTALLED:
#
#   argon2-cffi-bindi~ pkgs/main/win-64::argon2-cffi-bindings-21.2.0-py39h2bbff1b_0
#   asttokens          pkgs/main/noarch::asttokens-2.0.5-pyhd3eb1b0_0
#   executing          pkgs/main/noarch::executing-0.8.3-pyhd3eb1b0_0
#   pure_eval          pkgs/main/noarch::pure_eval-0.2.2-pyhd3eb1b0_0
#   python-fastjsonsc~ pkgs/main/noarch::python-fastjsonschema-2.15.1-pyhd3eb1b0_0
#   stack_data         pkgs/main/noarch::stack_data-0.2.0-pyhd3eb1b0_0
#   typing-extensions  pkgs/main/noarch::typing-extensions-4.1.1-hd3eb1b0_0
#   websocket-client   pkgs/main/win-64::websocket-client-0.58.0-py39haa95532_4
#
# The following packages will be REMOVED:
#
#   alabaster-0.7.12-pyhd3eb1b0_0
#   anaconda-2021.11-py39_0
#   anaconda-project-0.10.1-pyhd3eb1b0_0
#   appdirs-1.4.4-pyhd3eb1b0_0
#   argh-0.26.2-py39haa95532_0
#   arrow-0.13.1-py39haa95532_0
#   asn1crypto-1.4.0-py_0
#   astroid-2.6.6-py39haa95532_0
#   astropy-4.3.1-py39hc7d831d_0
#   async_generator-1.10-pyhd3eb1b0_0
#   atomicwrites-1.4.0-py_0
#   autopep8-1.5.7-pyhd3eb1b0_0
#   backports.shutil_get_terminal_size-1.0.0-pyhd3eb1b0_3
#   bcrypt-3.2.0-py39h196d8e1_0
#   binaryornot-0.4.4-pyhd3eb1b0_1
#   bitarray-2.3.0-py39h2bbff1b_1
#   bkcharts-0.2-py39haa95532_0
#   black-19.10b0-py_0
#   blas-1.0-mkl
#   blosc-1.21.0-h19a0ad4_0
#   bokeh-2.4.1-py39haa95532_0
#   boto-2.49.0-py39haa95532_0
#   bottleneck-1.3.2-py39h7cc1a96_1
#   brotli-1.0.9-ha925a31_2
#   cached-property-1.5.2-py_0
#   cfitsio-3.470-he774522_6
#   charls-2.2.0-h6c2663c_0
#   cloudpickle-2.0.0-pyhd3eb1b0_0
#   comtypes-1.1.10-py39haa95532_1002
#   conda-pack-0.6.0-pyhd3eb1b0_0
#   contextlib2-0.6.0.post1-pyhd3eb1b0_0
#   cookiecutter-1.7.2-pyhd3eb1b0_0
#   curl-7.78.0-h86230a5_0
#   cycler-0.10.0-py39haa95532_0
#   cython-0.29.24-py39h604cdb4_0
#   cytoolz-0.11.0-py39h2bbff1b_0
#   daal4py-2021.3.0-py39h757b272_0
#   dal-2021.3.0-haa95532_564
#   dask-2021.10.0-pyhd3eb1b0_0
#   dask-core-2021.10.0-pyhd3eb1b0_0
#   dataclasses-0.8-pyh6d0b6a4_7
#   diff-match-patch-20200713-pyhd3eb1b0_0
#   distributed-2021.10.0-py39haa95532_0
#   docutils-0.17.1-py39haa95532_1
#   et_xmlfile-1.1.0-py39haa95532_0
#   fastcache-1.1.0-py39h196d8e1_0
#   flake8-3.9.2-pyhd3eb1b0_0
#   flask-1.1.2-pyhd3eb1b0_0
#   fonttools-4.25.0-pyhd3eb1b0_0
#   fsspec-2021.10.1-pyhd3eb1b0_0
#   get_terminal_size-1.0.0-h38e98db_0
#   gevent-21.8.0-py39h2bbff1b_1
#   giflib-5.2.1-h62dcd97_0
#   greenlet-1.1.1-py39hd77b12b_0
#   h5py-3.2.1-py39h3de5c98_0
#   hdf5-1.10.6-h7ebc959_0
#   heapdict-1.0.1-pyhd3eb1b0_0
#   html5lib-1.1-pyhd3eb1b0_0
#   icc_rt-2019.0.0-h0cc432a_1
#   imagecodecs-2021.8.26-py39ha1f97ea_0
#   imageio-2.9.0-pyhd3eb1b0_0
#   imagesize-1.2.0-pyhd3eb1b0_0
#   importlib-metadata-4.8.1-py39haa95532_0
#   importlib_metadata-4.8.1-hd3eb1b0_0
#   inflection-0.5.1-py39haa95532_0
#   iniconfig-1.1.1-pyhd3eb1b0_0
#   intel-openmp-2021.4.0-haa95532_3556
#   intervaltree-3.1.0-pyhd3eb1b0_0
#   isort-5.9.3-pyhd3eb1b0_0
#   itsdangerous-2.0.1-pyhd3eb1b0_0
#   jdcal-1.4.1-pyhd3eb1b0_0
#   jinja2-time-0.2.0-pyhd3eb1b0_2
#   joblib-1.1.0-pyhd3eb1b0_0
#   jupyter-1.0.0-py39haa95532_7
#   jupyter_console-6.4.0-pyhd3eb1b0_0
#   keyring-23.1.0-py39haa95532_0
#   kiwisolver-1.3.1-py39hd77b12b_0
#   krb5-1.19.2-h5b6d351_0
#   lazy-object-proxy-1.6.0-py39h2bbff1b_0
#   lcms2-2.12-h83e58a3_0
#   lerc-3.0-hd77b12b_0
#   libaec-1.0.4-h33f27b4_1
#   libcurl-7.78.0-h86230a5_0
#   libdeflate-1.8-h2bbff1b_5
#   libspatialindex-1.9.3-h6c2663c_0
#   libssh2-1.9.0-h7a1dbc1_1
#   libxslt-1.1.34-he774522_0
#   libzopfli-1.0.3-ha925a31_0
#   llvmlite-0.37.0-py39h23ce68f_1
#   locket-0.2.1-py39haa95532_1
#   lxml-4.6.3-py39h9b66d53_0
#   lzo-2.10-he774522_2
#   m2w64-gcc-libgfortran-5.3.0-6
#   m2w64-gcc-libs-5.3.0-7
#   m2w64-gcc-libs-core-5.3.0-7
#   m2w64-gmp-6.1.0-2
#   m2w64-libwinpthread-git-5.0.0.4634.697f757-2
#   matplotlib-3.4.3-py39haa95532_0
#   matplotlib-base-3.4.3-py39h49ac443_0
#   mccabe-0.6.1-py39haa95532_1
#   mkl-2021.4.0-haa95532_640
#   mkl-service-2.4.0-py39h2bbff1b_0
#   mkl_fft-1.3.1-py39h277e83a_0
#   mkl_random-1.2.2-py39hf11a4ad_0
#   mock-4.0.3-pyhd3eb1b0_0
#   more-itertools-8.10.0-pyhd3eb1b0_0
#   mpmath-1.2.1-py39haa95532_0
#   msgpack-python-1.0.2-py39h59b6b97_1
#   msys2-conda-epoch-20160418-1
#   multipledispatch-0.6.0-py39haa95532_0
#   munkres-1.1.4-py_0
#   mypy_extensions-0.4.3-py39haa95532_0
#   networkx-2.6.3-pyhd3eb1b0_0
#   nltk-3.6.5-pyhd3eb1b0_0
#   nose-1.3.7-pyhd3eb1b0_1006
#   numba-0.54.1-py39hf11a4ad_0
#   numexpr-2.7.3-py39hb80d3ca_1
#   numpy-1.20.3-py39ha4e8547_0
#   numpy-base-1.20.3-py39hc2deb75_0
#   numpydoc-1.1.0-pyhd3eb1b0_1
#   olefile-0.46-pyhd3eb1b0_0
#   openjpeg-2.4.0-h4fc8c34_0
#   openpyxl-3.0.9-pyhd3eb1b0_0
#   pandas-1.3.4-py39h6214cd6_0
#   paramiko-2.7.2-py_0
#   partd-1.2.0-pyhd3eb1b0_0
#   path-16.0.0-py39haa95532_0
#   path.py-12.5.0-hd3eb1b0_0
#   pathlib2-2.3.6-py39haa95532_2
#   pathspec-0.7.0-py_0
#   patsy-0.5.2-py39haa95532_0
#   pep8-1.7.1-py39haa95532_0
#   pexpect-4.8.0-pyhd3eb1b0_3
#   pluggy-0.13.1-py39haa95532_0
#   ply-3.11-py39haa95532_0
#   poyo-0.5.0-pyhd3eb1b0_0
#   prompt_toolkit-3.0.20-hd3eb1b0_0
#   ptyprocess-0.7.0-pyhd3eb1b0_2
#   py-1.10.0-pyhd3eb1b0_0
#   pycodestyle-2.7.0-pyhd3eb1b0_0
#   pycurl-7.44.1-py39hcd4344a_1
#   pydocstyle-6.1.1-pyhd3eb1b0_0
#   pyerfa-2.0.0-py39h2bbff1b_0
#   pyflakes-2.3.1-pyhd3eb1b0_0
#   pylint-2.9.6-py39haa95532_1
#   pyls-spyder-0.4.0-pyhd3eb1b0_0
#   pynacl-1.4.0-py39hbd8134f_1
#   pyodbc-4.0.31-py39hd77b12b_0
#   pyreadline-2.1-py39haa95532_1
#   pytables-3.6.1-py39h56d22b6_1
#   pytest-6.2.4-py39haa95532_2
#   python-lsp-black-1.0.0-pyhd3eb1b0_0
#   python-lsp-jsonrpc-1.0.0-pyhd3eb1b0_0
#   python-lsp-server-1.2.4-pyhd3eb1b0_0
#   python-slugify-5.0.2-pyhd3eb1b0_0
#   pywavelets-1.1.1-py39h080aedc_4
#   pywin32-ctypes-0.2.0-py39haa95532_1000
#   qdarkstyle-3.0.2-pyhd3eb1b0_0
#   qstylizer-0.1.10-pyhd3eb1b0_0
#   qtawesome-1.0.2-pyhd3eb1b0_0
#   qtconsole-5.1.1-pyhd3eb1b0_0
#   regex-2021.8.3-py39h2bbff1b_0
#   rope-0.19.0-pyhd3eb1b0_0
#   rtree-0.9.7-py39h2eaa2aa_1
#   scikit-image-0.18.3-py39hf11a4ad_0
#   scikit-learn-0.24.2-py39hf11a4ad_1
#   scikit-learn-intelex-2021.3.0-py39haa95532_0
#   scipy-1.7.1-py39hbe87c03_2
#   seaborn-0.11.2-pyhd3eb1b0_0
#   simplegeneric-0.8.1-py39haa95532_2
#   singledispatch-3.7.0-pyhd3eb1b0_1001
#   snappy-1.1.8-h33f27b4_0
#   snowballstemmer-2.1.0-pyhd3eb1b0_0
#   sortedcollections-2.1.0-pyhd3eb1b0_0
#   sortedcontainers-2.4.0-pyhd3eb1b0_0
#   sphinx-4.2.0-pyhd3eb1b0_1
#   sphinxcontrib-1.0-py39haa95532_1
#   sphinxcontrib-applehelp-1.0.2-pyhd3eb1b0_0
#   sphinxcontrib-devhelp-1.0.2-pyhd3eb1b0_0
#   sphinxcontrib-htmlhelp-2.0.0-pyhd3eb1b0_0
#   sphinxcontrib-jsmath-1.0.1-pyhd3eb1b0_0
#   sphinxcontrib-qthelp-1.0.3-pyhd3eb1b0_0
#   sphinxcontrib-serializinghtml-1.1.5-pyhd3eb1b0_0
#   sphinxcontrib-websupport-1.2.4-py_0
#   spyder-5.1.5-py39haa95532_1
#   spyder-kernels-2.1.3-py39haa95532_0
#   sqlalchemy-1.4.22-py39h2bbff1b_0
#   statsmodels-0.12.2-py39h2bbff1b_0
#   sympy-1.9-py39haa95532_0
#   tbb-2021.4.0-h59b6b97_0
#   tbb4py-2021.4.0-py39h59b6b97_0
#   tblib-1.7.0-pyhd3eb1b0_0
#   text-unidecode-1.3-pyhd3eb1b0_0
#   textdistance-4.2.1-pyhd3eb1b0_0
#   threadpoolctl-2.2.0-pyh0d69192_0
#   three-merge-0.1.1-pyhd3eb1b0_0
#   tifffile-2021.7.2-pyhd3eb1b0_2
#   tinycss-0.4-pyhd3eb1b0_1002
#   toml-0.10.2-pyhd3eb1b0_0
#   toolz-0.11.1-pyhd3eb1b0_0
#   typed-ast-1.4.3-py39h2bbff1b_1
#   unicodecsv-0.14.1-py39haa95532_0
#   unidecode-1.2.0-pyhd3eb1b0_0
#   watchdog-2.1.3-py39haa95532_0
#   werkzeug-2.0.2-pyhd3eb1b0_0
#   whichcraft-0.6.1-pyhd3eb1b0_0
#   win_unicode_console-0.5-py39haa95532_0
#   wrapt-1.12.1-py39h196d8e1_1
#   xlrd-2.0.1-pyhd3eb1b0_0
#   xlsxwriter-3.0.1-pyhd3eb1b0_0
#   xlwings-0.24.9-py39haa95532_0
#   xlwt-1.3.0-py39haa95532_0
#   yapf-0.31.0-pyhd3eb1b0_0
#   zfp-0.5.5-hd77b12b_6
#   zict-2.0.0-pyhd3eb1b0_0
#   zipp-3.6.0-pyhd3eb1b0_0
#   zope-1.0-py39haa95532_1
#   zope.event-4.5.0-py39haa95532_0
#   zope.interface-5.4.0-py39h2bbff1b_0
#
# The following packages will be UPDATED:
#
#   anaconda-client                      1.9.0-py39haa95532_0 --> 1.10.0-py39haa95532_0
#   anyio                                2.2.0-py39haa95532_2 --> 3.5.0-py39haa95532_0
#   argon2-cffi        pkgs/main/win-64::argon2-cffi-20.1.0-~ --> pkgs/main/noarch::argo
# n2-cffi-21.3.0-pyhd3eb1b0_0
#   attrs                                 21.2.0-pyhd3eb1b0_0 --> 21.4.0-pyhd3eb1b0_0
#   backports                                1.0-pyhd3eb1b0_2 --> 1.1-pyhd3eb1b0_0
#   beautifulsoup4     pkgs/main/noarch::beautifulsoup4-4.10~ --> pkgs/main/win-64::beau
# tifulsoup4-4.11.1-py39haa95532_0
#   bleach                                 4.0.0-pyhd3eb1b0_0 --> 4.1.0-pyhd3eb1b0_0
#   ca-certificates                     2021.10.26-haa95532_2 --> 2022.4.26-haa95532_0
#   certifi                          2021.10.8-py39haa95532_0 --> 2022.6.15-py39haa95532
# _0
#   cffi                                1.14.6-py39h2bbff1b_0 --> 1.15.0-py39h2bbff1b_1
#   click              pkgs/main/noarch::click-8.0.3-pyhd3eb~ --> pkgs/main/win-64::clic
# k-8.0.4-py39haa95532_0
#   conda-build                         3.21.6-py39haa95532_0 --> 3.21.9-py39haa95532_0
#   debugpy                              1.4.1-py39hd77b12b_0 --> 1.5.1-py39hd77b12b_0
#   decorator                              5.1.0-pyhd3eb1b0_0 --> 5.1.1-pyhd3eb1b0_0
#   entrypoints                            0.3-py39haa95532_0 --> 0.4-py39haa95532_0
#   filelock                               3.3.1-pyhd3eb1b0_1 --> 3.6.0-pyhd3eb1b0_0
#   idna                                     3.2-pyhd3eb1b0_0 --> 3.3-pyhd3eb1b0_0
#   ipykernel                            6.4.1-py39haa95532_1 --> 6.9.1-py39haa95532_0
#   ipython                             7.29.0-py39hd4e2768_0 --> 8.3.0-py39haa95532_0
#   jedi                                0.18.0-py39haa95532_1 --> 0.18.1-py39haa95532_1
#   jpeg                                        9d-h2bbff1b_0 --> 9e-h2bbff1b_0
#   jsonschema         pkgs/main/noarch::jsonschema-3.2.0-py~ --> pkgs/main/win-64::json
# schema-4.4.0-py39haa95532_0
#   jupyter_client     pkgs/main/noarch::jupyter_client-6.1.~ --> pkgs/main/win-64::jupy
# ter_client-7.2.2-py39haa95532_0
#   jupyter_core                         4.8.1-py39haa95532_0 --> 4.10.0-py39haa95532_0
#   jupyter_server                       1.4.1-py39haa95532_0 --> 1.17.1-py39haa95532_0
#   jupyterlab                             3.2.1-pyhd3eb1b0_1 --> 3.3.2-pyhd3eb1b0_0
#   jupyterlab_server                      2.8.2-pyhd3eb1b0_0 --> 2.10.3-pyhd3eb1b0_1
#   libarchive                               3.4.2-h5e25573_0 --> 3.5.2-h214662b_0
#   libiconv                                  1.15-h1df5818_7 --> 1.16-h2bbff1b_2
#   liblief                                 0.10.1-hd77b12b_1 --> 0.11.5-hd77b12b_1
#   libtiff                                  4.2.0-hd0e1b90_0 --> 4.2.0-he0120a3_1
#   libwebp                                  1.2.0-h2bbff1b_0 --> 1.2.2-h2bbff1b_0
#   libxml2                                 2.9.12-h0ad7f3c_0 --> 2.9.14-h0ad7f3c_0
#   markupsafe                           1.1.1-py39h2bbff1b_0 --> 2.0.1-py39h2bbff1b_0
#   nbclassic                              0.2.6-pyhd3eb1b0_0 --> 0.3.5-pyhd3eb1b0_0
#   nbclient           pkgs/main/noarch::nbclient-0.5.3-pyhd~ --> pkgs/main/win-64::nbcl
# ient-0.5.13-py39haa95532_0
#   nbconvert                            6.1.0-py39haa95532_0 --> 6.4.4-py39haa95532_0
#   nbformat           pkgs/main/noarch::nbformat-5.1.3-pyhd~ --> pkgs/main/win-64::nbfo
# rmat-5.3.0-py39haa95532_0
#   nest-asyncio       pkgs/main/noarch::nest-asyncio-1.5.1-~ --> pkgs/main/win-64::nest
# -asyncio-1.5.5-py39haa95532_0
#   notebook                             6.4.5-py39haa95532_0 --> 6.4.11-py39haa95532_0
#   openssl                                 1.1.1l-h2bbff1b_0 --> 1.1.1p-h2bbff1b_0
#   packaging                               21.0-pyhd3eb1b0_0 --> 21.3-pyhd3eb1b0_0
#   pandocfilters      pkgs/main/win-64::pandocfilters-1.4.3~ --> pkgs/main/noarch::pand
# ocfilters-1.5.0-pyhd3eb1b0_0
#   parso                                  0.8.2-pyhd3eb1b0_0 --> 0.8.3-pyhd3eb1b0_0
#   pillow                               8.4.0-py39hd45dc43_0 --> 9.0.1-py39hdc2b20a_0
#   pkginfo            pkgs/main/win-64::pkginfo-1.7.1-py39h~ --> pkgs/main/noarch::pkgi
# nfo-1.8.2-pyhd3eb1b0_0
#   prometheus_client                     0.11.0-pyhd3eb1b0_0 --> 0.13.1-pyhd3eb1b0_0
#   psutil                               5.8.0-py39h2bbff1b_1 --> 5.9.0-py39h2bbff1b_0
#   py-lief                             0.10.1-py39hd77b12b_1 --> 0.11.5-py39hd77b12b_1
#   pycparser                                       2.20-py_2 --> 2.21-pyhd3eb1b0_0
#   pygments                              2.10.0-pyhd3eb1b0_0 --> 2.11.2-pyhd3eb1b0_0
#   pytz               pkgs/main/noarch::pytz-2021.3-pyhd3eb~ --> pkgs/main/win-64::pytz
# -2022.1-py39haa95532_0
#   pywin32                                228-py39he774522_0 --> 302-py39h2bbff1b_2
#   pywinpty                             0.5.7-py39haa95532_0 --> 2.0.2-py39h5da7b33_0
#   pyzmq                               22.2.1-py39hd77b12b_1 --> 22.3.0-py39hd77b12b_2
#   qtpy                                  1.10.0-pyhd3eb1b0_0 --> 2.0.1-pyhd3eb1b0_0
#   requests           pkgs/main/noarch::requests-2.26.0-pyh~ --> pkgs/main/win-64::requ
# ests-2.28.0-py39haa95532_0
#   setuptools                          58.0.4-py39haa95532_0 --> 61.2.0-py39haa95532_0
#   six                                   1.16.0-pyhd3eb1b0_0 --> 1.16.0-pyhd3eb1b0_1
#   soupsieve                              2.2.1-pyhd3eb1b0_0 --> 2.3.1-pyhd3eb1b0_0
#   sqlite                                  3.36.0-h2bbff1b_0 --> 3.38.5-h2bbff1b_0
#   terminado                            0.9.4-py39haa95532_0 --> 0.13.1-py39haa95532_0
#   testpath           pkgs/main/noarch::testpath-0.5.0-pyhd~ --> pkgs/main/win-64::test
# path-0.6.0-py39haa95532_0
#   tk                                      8.6.11-h2bbff1b_0 --> 8.6.12-h2bbff1b_0
#   tqdm               pkgs/main/noarch::tqdm-4.62.3-pyhd3eb~ --> pkgs/main/win-64::tqdm
# -4.64.0-py39haa95532_0
#   traitlets                              5.1.0-pyhd3eb1b0_0 --> 5.1.1-pyhd3eb1b0_0
#   typing_extensions                   3.10.0.2-pyh06a4308_0 --> 4.1.1-pyh06a4308_0
#   tzdata                                   2021e-hda174b7_0 --> 2022a-hda174b7_0
#   ujson                                4.0.2-py39hd77b12b_0 --> 5.1.0-py39hd77b12b_0
#   urllib3            pkgs/main/noarch::urllib3-1.26.7-pyhd~ --> pkgs/main/win-64::urll
# ib3-1.26.9-py39haa95532_0
#   wheel                                 0.37.0-pyhd3eb1b0_1 --> 0.37.1-pyhd3eb1b0_0
#   widgetsnbextension                   3.5.1-py39haa95532_0 --> 3.5.2-py39haa95532_0
#   xz                                       5.2.5-h62dcd97_0 --> 5.2.5-h8cc25b3_1
#   zlib                                    1.2.11-h62dcd97_4 --> 1.2.12-h8cc25b3_2
#   zstd                                     1.4.9-h19a0ad4_0 --> 1.5.2-h19a0ad4_0
#
#
# Proceed ([y]/n)? y
#
#
# Downloading and Extracting Packages
# libiconv-1.16        | 651 KB    | ########################################## | 100%
# executing-0.8.3      | 18 KB     | ########################################## | 100%
# wheel-0.37.1         | 33 KB     | ########################################## | 100%
# urllib3-1.26.9       | 190 KB    | ########################################## | 100%
# jupyterlab-3.3.2     | 3.6 MB    | ########################################## | 100%
# backports-1.1        | 4 KB      | ########################################## | 100%
# anyio-3.5.0          | 167 KB    | ########################################## | 100%
# idna-3.3             | 49 KB     | ########################################## | 100%
# anaconda-client-1.10 | 166 KB    | ########################################## | 100%
# jsonschema-4.4.0     | 139 KB    | ########################################## | 100%
# pywin32-302          | 5.6 MB    | ########################################## | 100%
# pandocfilters-1.5.0  | 11 KB     | ########################################## | 100%
# nbformat-5.3.0       | 146 KB    | ########################################## | 100%
# ipython-8.3.0        | 1010 KB   | ########################################## | 100%
# libarchive-3.5.2     | 781 KB    | ########################################## | 100%
# pytz-2022.1          | 195 KB    | ########################################## | 100%
# zstd-1.5.2           | 509 KB    | ########################################## | 100%
# traitlets-5.1.1      | 84 KB     | ########################################## | 100%
# pywinpty-2.0.2       | 200 KB    | ########################################## | 100%
# six-1.16.0           | 18 KB     | ########################################## | 100%
# beautifulsoup4-4.11. | 190 KB    | ########################################## | 100%
# jedi-0.18.1          | 982 KB    | ########################################## | 100%
# jpeg-9e              | 292 KB    | ########################################## | 100%
# typing-extensions-4. | 8 KB      | ########################################## | 100%
# widgetsnbextension-3 | 646 KB    | ########################################## | 100%
# attrs-21.4.0         | 51 KB     | ########################################## | 100%
# liblief-0.11.5       | 2.1 MB    | ########################################## | 100%
# testpath-0.6.0       | 85 KB     | ########################################## | 100%
# libxml2-2.9.14       | 1.5 MB    | ########################################## | 100%
# pillow-9.0.1         | 921 KB    | ########################################## | 100%
# psutil-5.9.0         | 349 KB    | ########################################## | 100%
# zlib-1.2.12          | 116 KB    | ########################################## | 100%
# openssl-1.1.1p       | 4.8 MB    | ########################################## | 100%
# bleach-4.1.0         | 123 KB    | ########################################## | 100%
# prometheus_client-0. | 47 KB     | ########################################## | 100%
# debugpy-1.5.1        | 2.6 MB    | ########################################## | 100%
# pygments-2.11.2      | 759 KB    | ########################################## | 100%
# python-fastjsonschem | 29 KB     | ########################################## | 100%
# requests-2.28.0      | 100 KB    | ########################################## | 100%
# websocket-client-0.5 | 69 KB     | ########################################## | 100%
# argon2-cffi-bindings | 36 KB     | ########################################## | 100%
# stack_data-0.2.0     | 22 KB     | ########################################## | 100%
# jupyter_server-1.17. | 374 KB    | ########################################## | 100%
# markupsafe-2.0.1     | 24 KB     | ########################################## | 100%
# libwebp-1.2.2        | 658 KB    | ########################################## | 100%
# asttokens-2.0.5      | 20 KB     | ########################################## | 100%
# parso-0.8.3          | 70 KB     | ########################################## | 100%
# decorator-5.1.1      | 12 KB     | ########################################## | 100%
# filelock-3.6.0       | 12 KB     | ########################################## | 100%
# jupyterlab_server-2. | 48 KB     | ########################################## | 100%
# pycparser-2.21       | 94 KB     | ########################################## | 100%
# tk-8.6.12            | 3.1 MB    | ########################################## | 100%
# nbclassic-0.3.5      | 22 KB     | ########################################## | 100%
# soupsieve-2.3.1      | 34 KB     | ########################################## | 100%
# click-8.0.4          | 155 KB    | ########################################## | 100%
# typing_extensions-4. | 28 KB     | ########################################## | 100%
# pyzmq-22.3.0         | 632 KB    | ########################################## | 100%
# ipykernel-6.9.1      | 200 KB    | ########################################## | 100%
# conda-build-3.21.9   | 555 KB    | ########################################## | 100%
# jupyter_client-7.2.2 | 216 KB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# nbclient-0.5.13      | 108 KB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# py-lief-0.11.5       | 1.7 MB    | ########################################## | 100%
# nbclient-0.5.13      | 108 KB    | ########################################## | 100%
# packaging-21.3       | 36 KB     | ########################################## | 100%
# tzdata-2022a         | 109 KB    | ########################################## | 100%
# pure_eval-0.2.2      | 14 KB     | ########################################## | 100%
# xz-5.2.5             | 246 KB    | ########################################## | 100%
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda install numpy=1.20.1
# Collecting package metadata (current_repodata.json): done
# Solving environment: failed with initial frozen solve. Retrying with flexible solve.
# Collecting package metadata (repodata.json): done
# Solving environment: done
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3
#
#   added / updated specs:
#     - numpy=1.20.1
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     numpy-1.20.1               |   py39h34a8a5c_0          23 KB
#     numpy-base-1.20.1          |   py39haf7ebc8_0         4.2 MB
#     ------------------------------------------------------------
#                                            Total:         4.2 MB
#
# The following NEW packages will be INSTALLED:
#
#   blas               pkgs/main/win-64::blas-1.0-mkl
#   intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
#   mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
#   mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
#   mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
#   mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
#   numpy              pkgs/main/win-64::numpy-1.20.1-py39h34a8a5c_0
#   numpy-base         pkgs/main/win-64::numpy-base-1.20.1-py39haf7ebc8_0
#
# Proceed ([y]/n)? y
#
#
# Downloading and Extracting Packages
# numpy-base-1.20.1    | 4.2 MB    | ########################################## | 100%
# numpy-1.20.1         | 23 KB     | ########################################## | 100%
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda list
# # packages in environment at C:\Users\aleyy\anaconda3:
# #
# # Name                    Version                   Build  Channel
# _ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
# anaconda-client           1.10.0           py39haa95532_0
# anaconda-navigator        2.1.1                    py39_0
# anyio                     3.5.0            py39haa95532_0
# argon2-cffi               21.3.0             pyhd3eb1b0_0
# argon2-cffi-bindings      21.2.0           py39h2bbff1b_0
# asttokens                 2.0.5              pyhd3eb1b0_0
# attrs                     21.4.0             pyhd3eb1b0_0
# babel                     2.9.1              pyhd3eb1b0_0
# backcall                  0.2.0              pyhd3eb1b0_0
# backports                 1.1                pyhd3eb1b0_0
# backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
# backports.tempfile        1.0                pyhd3eb1b0_1
# backports.weakref         1.0.post1                  py_1
# beautifulsoup4            4.11.1           py39haa95532_0
# blas                      1.0                         mkl
# bleach                    4.1.0              pyhd3eb1b0_0
# brotlipy                  0.7.0           py39h2bbff1b_1003
# bzip2                     1.0.8                he774522_0
# ca-certificates           2022.4.26            haa95532_0
# certifi                   2022.6.15        py39haa95532_0
# cffi                      1.15.0           py39h2bbff1b_1
# chardet                   4.0.0           py39haa95532_1003
# charset-normalizer        2.0.4              pyhd3eb1b0_0
# click                     8.0.4            py39haa95532_0
# clyent                    1.2.2            py39haa95532_1
# colorama                  0.4.4              pyhd3eb1b0_0
# conda                     4.13.0           py39haa95532_0
# conda-build               3.21.9           py39haa95532_0
# conda-content-trust       0.1.1              pyhd3eb1b0_0
# conda-env                 2.6.0                         1
# conda-package-handling    1.8.1            py39h8cc25b3_0
# conda-repo-cli            1.0.4              pyhd3eb1b0_0
# conda-token               0.3.0              pyhd3eb1b0_0
# conda-verify              3.4.2                      py_1
# console_shortcut          0.1.1                         4
# cryptography              3.4.8            py39h71e12ea_0
# debugpy                   1.5.1            py39hd77b12b_0
# decorator                 5.1.1              pyhd3eb1b0_0
# defusedxml                0.7.1              pyhd3eb1b0_0
# entrypoints               0.4              py39haa95532_0
# executing                 0.8.3              pyhd3eb1b0_0
# filelock                  3.6.0              pyhd3eb1b0_0
# freetype                  2.10.4               hd328e21_0
# future                    0.18.2           py39haa95532_1
# glob2                     0.7                pyhd3eb1b0_0
# icu                       58.2                 ha925a31_3
# idna                      3.3                pyhd3eb1b0_0
# intel-openmp              2021.4.0          haa95532_3556
# ipykernel                 6.9.1            py39haa95532_0
# ipython                   8.3.0            py39haa95532_0
# ipython_genutils          0.2.0              pyhd3eb1b0_1
# ipywidgets                7.6.5              pyhd3eb1b0_1
# jedi                      0.18.1           py39haa95532_1
# jinja2                    2.11.3             pyhd3eb1b0_0
# jpeg                      9e                   h2bbff1b_0
# json5                     0.9.6              pyhd3eb1b0_0
# jsonschema                4.4.0            py39haa95532_0
# jupyter_client            7.2.2            py39haa95532_0
# jupyter_core              4.10.0           py39haa95532_0
# jupyter_server            1.17.1           py39haa95532_0
# jupyterlab                3.3.2              pyhd3eb1b0_0
# jupyterlab_pygments       0.1.2                      py_0
# jupyterlab_server         2.10.3             pyhd3eb1b0_1
# jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
# libarchive                3.5.2                h214662b_0
# libiconv                  1.16                 h2bbff1b_2
# liblief                   0.11.5               hd77b12b_1
# libpng                    1.6.37               h2a8f88b_0
# libtiff                   4.2.0                he0120a3_1
# libwebp                   1.2.2                h2bbff1b_0
# libxml2                   2.9.14               h0ad7f3c_0
# lz4-c                     1.9.3                h2bbff1b_1
# markupsafe                2.0.1            py39h2bbff1b_0
# matplotlib-inline         0.1.2              pyhd3eb1b0_2
# menuinst                  1.4.18           py39h59b6b97_0
# mistune                   0.8.4           py39h2bbff1b_1000
# mkl                       2021.4.0           haa95532_640
# mkl-service               2.4.0            py39h2bbff1b_0
# mkl_fft                   1.3.1            py39h277e83a_0
# mkl_random                1.2.2            py39hf11a4ad_0
# navigator-updater         0.2.1            py39haa95532_0
# nbclassic                 0.3.5              pyhd3eb1b0_0
# nbclient                  0.5.13           py39haa95532_0
# nbconvert                 6.4.4            py39haa95532_0
# nbformat                  5.3.0            py39haa95532_0
# nest-asyncio              1.5.5            py39haa95532_0
# notebook                  6.4.11           py39haa95532_0
# numpy                     1.20.1           py39h34a8a5c_0
# numpy-base                1.20.1           py39haf7ebc8_0
# openssl                   1.1.1p               h2bbff1b_0
# packaging                 21.3               pyhd3eb1b0_0
# pandocfilters             1.5.0              pyhd3eb1b0_0
# parso                     0.8.3              pyhd3eb1b0_0
# pickleshare               0.7.5           pyhd3eb1b0_1003
# pillow                    9.0.1            py39hdc2b20a_0
# pip                       21.2.4           py39haa95532_0
# pkginfo                   1.8.2              pyhd3eb1b0_0
# powershell_shortcut       0.0.1                         3
# prometheus_client         0.13.1             pyhd3eb1b0_0
# prompt-toolkit            3.0.20             pyhd3eb1b0_0
# psutil                    5.9.0            py39h2bbff1b_0
# pure_eval                 0.2.2              pyhd3eb1b0_0
# py-lief                   0.11.5           py39hd77b12b_1
# pycosat                   0.6.3            py39h2bbff1b_0
# pycparser                 2.21               pyhd3eb1b0_0
# pygments                  2.11.2             pyhd3eb1b0_0
# pyjwt                     2.1.0            py39haa95532_0
# pyopenssl                 21.0.0             pyhd3eb1b0_1
# pyparsing                 3.0.4              pyhd3eb1b0_0
# pyqt                      5.9.2            py39hd77b12b_6
# pyrsistent                0.18.0           py39h196d8e1_0
# pysocks                   1.7.1            py39haa95532_0
# python                    3.9.7                h6244533_1
# python-dateutil           2.8.2              pyhd3eb1b0_0
# python-fastjsonschema     2.15.1             pyhd3eb1b0_0
# python-libarchive-c       2.9                pyhd3eb1b0_1
# pytz                      2022.1           py39haa95532_0
# pywin32                   302              py39h2bbff1b_2
# pywinpty                  2.0.2            py39h5da7b33_0
# pyyaml                    6.0              py39h2bbff1b_1
# pyzmq                     22.3.0           py39hd77b12b_2
# qt                        5.9.7            vc14h73c81de_0
# qtpy                      2.0.1              pyhd3eb1b0_0
# requests                  2.28.0           py39haa95532_0
# ruamel_yaml               0.15.100         py39h2bbff1b_0
# send2trash                1.8.0              pyhd3eb1b0_1
# setuptools                61.2.0           py39haa95532_0
# sip                       4.19.13          py39hd77b12b_0
# six                       1.16.0             pyhd3eb1b0_1
# sniffio                   1.2.0            py39haa95532_1
# soupsieve                 2.3.1              pyhd3eb1b0_0
# sqlite                    3.38.5               h2bbff1b_0
# stack_data                0.2.0              pyhd3eb1b0_0
# terminado                 0.13.1           py39haa95532_0
# testpath                  0.6.0            py39haa95532_0
# tk                        8.6.12               h2bbff1b_0
# tornado                   6.1              py39h2bbff1b_0
# tqdm                      4.64.0           py39haa95532_0
# traitlets                 5.1.1              pyhd3eb1b0_0
# typing-extensions         4.1.1                hd3eb1b0_0
# typing_extensions         4.1.1              pyh06a4308_0
# tzdata                    2022a                hda174b7_0
# ujson                     5.1.0            py39hd77b12b_0
# urllib3                   1.26.9           py39haa95532_0
# vc                        14.2                 h21ff451_1
# vs2015_runtime            14.27.29016          h5e58377_2
# wcwidth                   0.2.5              pyhd3eb1b0_0
# webencodings              0.5.1            py39haa95532_1
# websocket-client          0.58.0           py39haa95532_4
# widgetsnbextension        3.5.2            py39haa95532_0
# win_inet_pton             1.1.0            py39haa95532_0
# wincertstore              0.2              py39haa95532_2
# winpty                    0.4.3                         4
# xmltodict                 0.12.0             pyhd3eb1b0_0
# xz                        5.2.5                h8cc25b3_1
# yaml                      0.2.5                he774522_0
# zlib                      1.2.12               h8cc25b3_2
# zstd                      1.5.2                h19a0ad4_0
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda upgrade numpy
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3
#
#   added / updated specs:
#     - numpy
#
#
# The following packages will be downloaded:
#
#     package                    |            build
#     ---------------------------|-----------------
#     numpy-1.22.3               |   py39h7a0a035_0          25 KB
#     numpy-base-1.22.3          |   py39hca35cd5_0         4.8 MB
#     ------------------------------------------------------------
#                                            Total:         4.9 MB
#
# The following packages will be UPDATED:
#
#   numpy                               1.20.1-py39h34a8a5c_0 --> 1.22.3-py39h7a0a035_0
#   numpy-base                          1.20.1-py39haf7ebc8_0 --> 1.22.3-py39hca35cd5_0
#
# Proceed ([y]/n)? y
#
#
# Downloading and Extracting Packages
# numpy-base-1.22.3    | 4.8 MB    | ########################################## | 100%
# numpy-1.22.3         | 25 KB     | ########################################## | 100%
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda list
# # packages in environment at C:\Users\aleyy\anaconda3:
# #
# # Name                    Version                   Build  Channel
# _ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
# anaconda-client           1.10.0           py39haa95532_0
# anaconda-navigator        2.1.1                    py39_0
# anyio                     3.5.0            py39haa95532_0
# argon2-cffi               21.3.0             pyhd3eb1b0_0
# argon2-cffi-bindings      21.2.0           py39h2bbff1b_0
# asttokens                 2.0.5              pyhd3eb1b0_0
# attrs                     21.4.0             pyhd3eb1b0_0
# babel                     2.9.1              pyhd3eb1b0_0
# backcall                  0.2.0              pyhd3eb1b0_0
# backports                 1.1                pyhd3eb1b0_0
# backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
# backports.tempfile        1.0                pyhd3eb1b0_1
# backports.weakref         1.0.post1                  py_1
# beautifulsoup4            4.11.1           py39haa95532_0
# blas                      1.0                         mkl
# bleach                    4.1.0              pyhd3eb1b0_0
# brotlipy                  0.7.0           py39h2bbff1b_1003
# bzip2                     1.0.8                he774522_0
# ca-certificates           2022.4.26            haa95532_0
# certifi                   2022.6.15        py39haa95532_0
# cffi                      1.15.0           py39h2bbff1b_1
# chardet                   4.0.0           py39haa95532_1003
# charset-normalizer        2.0.4              pyhd3eb1b0_0
# click                     8.0.4            py39haa95532_0
# clyent                    1.2.2            py39haa95532_1
# colorama                  0.4.4              pyhd3eb1b0_0
# conda                     4.13.0           py39haa95532_0
# conda-build               3.21.9           py39haa95532_0
# conda-content-trust       0.1.1              pyhd3eb1b0_0
# conda-env                 2.6.0                         1
# conda-package-handling    1.8.1            py39h8cc25b3_0
# conda-repo-cli            1.0.4              pyhd3eb1b0_0
# conda-token               0.3.0              pyhd3eb1b0_0
# conda-verify              3.4.2                      py_1
# console_shortcut          0.1.1                         4
# cryptography              3.4.8            py39h71e12ea_0
# debugpy                   1.5.1            py39hd77b12b_0
# decorator                 5.1.1              pyhd3eb1b0_0
# defusedxml                0.7.1              pyhd3eb1b0_0
# entrypoints               0.4              py39haa95532_0
# executing                 0.8.3              pyhd3eb1b0_0
# filelock                  3.6.0              pyhd3eb1b0_0
# freetype                  2.10.4               hd328e21_0
# future                    0.18.2           py39haa95532_1
# glob2                     0.7                pyhd3eb1b0_0
# icu                       58.2                 ha925a31_3
# idna                      3.3                pyhd3eb1b0_0
# intel-openmp              2021.4.0          haa95532_3556
# ipykernel                 6.9.1            py39haa95532_0
# ipython                   8.3.0            py39haa95532_0
# ipython_genutils          0.2.0              pyhd3eb1b0_1
# ipywidgets                7.6.5              pyhd3eb1b0_1
# jedi                      0.18.1           py39haa95532_1
# jinja2                    2.11.3             pyhd3eb1b0_0
# jpeg                      9e                   h2bbff1b_0
# json5                     0.9.6              pyhd3eb1b0_0
# jsonschema                4.4.0            py39haa95532_0
# jupyter_client            7.2.2            py39haa95532_0
# jupyter_core              4.10.0           py39haa95532_0
# jupyter_server            1.17.1           py39haa95532_0
# jupyterlab                3.3.2              pyhd3eb1b0_0
# jupyterlab_pygments       0.1.2                      py_0
# jupyterlab_server         2.10.3             pyhd3eb1b0_1
# jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
# libarchive                3.5.2                h214662b_0
# libiconv                  1.16                 h2bbff1b_2
# liblief                   0.11.5               hd77b12b_1
# libpng                    1.6.37               h2a8f88b_0
# libtiff                   4.2.0                he0120a3_1
# libwebp                   1.2.2                h2bbff1b_0
# libxml2                   2.9.14               h0ad7f3c_0
# lz4-c                     1.9.3                h2bbff1b_1
# markupsafe                2.0.1            py39h2bbff1b_0
# matplotlib-inline         0.1.2              pyhd3eb1b0_2
# menuinst                  1.4.18           py39h59b6b97_0
# mistune                   0.8.4           py39h2bbff1b_1000
# mkl                       2021.4.0           haa95532_640
# mkl-service               2.4.0            py39h2bbff1b_0
# mkl_fft                   1.3.1            py39h277e83a_0
# mkl_random                1.2.2            py39hf11a4ad_0
# navigator-updater         0.2.1            py39haa95532_0
# nbclassic                 0.3.5              pyhd3eb1b0_0
# nbclient                  0.5.13           py39haa95532_0
# nbconvert                 6.4.4            py39haa95532_0
# nbformat                  5.3.0            py39haa95532_0
# nest-asyncio              1.5.5            py39haa95532_0
# notebook                  6.4.11           py39haa95532_0
# numpy                     1.22.3           py39h7a0a035_0
# numpy-base                1.22.3           py39hca35cd5_0
# openssl                   1.1.1p               h2bbff1b_0
# packaging                 21.3               pyhd3eb1b0_0
# pandocfilters             1.5.0              pyhd3eb1b0_0
# parso                     0.8.3              pyhd3eb1b0_0
# pickleshare               0.7.5           pyhd3eb1b0_1003
# pillow                    9.0.1            py39hdc2b20a_0
# pip                       21.2.4           py39haa95532_0
# pkginfo                   1.8.2              pyhd3eb1b0_0
# powershell_shortcut       0.0.1                         3
# prometheus_client         0.13.1             pyhd3eb1b0_0
# prompt-toolkit            3.0.20             pyhd3eb1b0_0
# psutil                    5.9.0            py39h2bbff1b_0
# pure_eval                 0.2.2              pyhd3eb1b0_0
# py-lief                   0.11.5           py39hd77b12b_1
# pycosat                   0.6.3            py39h2bbff1b_0
# pycparser                 2.21               pyhd3eb1b0_0
# pygments                  2.11.2             pyhd3eb1b0_0
# pyjwt                     2.1.0            py39haa95532_0
# pyopenssl                 21.0.0             pyhd3eb1b0_1
# pyparsing                 3.0.4              pyhd3eb1b0_0
# pyqt                      5.9.2            py39hd77b12b_6
# pyrsistent                0.18.0           py39h196d8e1_0
# pysocks                   1.7.1            py39haa95532_0
# python                    3.9.7                h6244533_1
# python-dateutil           2.8.2              pyhd3eb1b0_0
# python-fastjsonschema     2.15.1             pyhd3eb1b0_0
# python-libarchive-c       2.9                pyhd3eb1b0_1
# pytz                      2022.1           py39haa95532_0
# pywin32                   302              py39h2bbff1b_2
# pywinpty                  2.0.2            py39h5da7b33_0
# pyyaml                    6.0              py39h2bbff1b_1
# pyzmq                     22.3.0           py39hd77b12b_2
# qt                        5.9.7            vc14h73c81de_0
# qtpy                      2.0.1              pyhd3eb1b0_0
# requests                  2.28.0           py39haa95532_0
# ruamel_yaml               0.15.100         py39h2bbff1b_0
# send2trash                1.8.0              pyhd3eb1b0_1
# setuptools                61.2.0           py39haa95532_0
# sip                       4.19.13          py39hd77b12b_0
# six                       1.16.0             pyhd3eb1b0_1
# sniffio                   1.2.0            py39haa95532_1
# soupsieve                 2.3.1              pyhd3eb1b0_0
# sqlite                    3.38.5               h2bbff1b_0
# stack_data                0.2.0              pyhd3eb1b0_0
# terminado                 0.13.1           py39haa95532_0
# testpath                  0.6.0            py39haa95532_0
# tk                        8.6.12               h2bbff1b_0
# tornado                   6.1              py39h2bbff1b_0
# tqdm                      4.64.0           py39haa95532_0
# traitlets                 5.1.1              pyhd3eb1b0_0
# typing-extensions         4.1.1                hd3eb1b0_0
# typing_extensions         4.1.1              pyh06a4308_0
# tzdata                    2022a                hda174b7_0
# ujson                     5.1.0            py39hd77b12b_0
# urllib3                   1.26.9           py39haa95532_0
# vc                        14.2                 h21ff451_1
# vs2015_runtime            14.27.29016          h5e58377_2
# wcwidth                   0.2.5              pyhd3eb1b0_0
# webencodings              0.5.1            py39haa95532_1
# websocket-client          0.58.0           py39haa95532_4
# widgetsnbextension        3.5.2            py39haa95532_0
# win_inet_pton             1.1.0            py39haa95532_0
# wincertstore              0.2              py39haa95532_2
# winpty                    0.4.3                         4
# xmltodict                 0.12.0             pyhd3eb1b0_0
# xz                        5.2.5                h8cc25b3_1
# yaml                      0.2.5                he774522_0
# zlib                      1.2.12               h8cc25b3_2
# zstd                      1.5.2                h19a0ad4_0
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> pip install pandas
# Collecting pandas
#   Downloading pandas-1.4.3-cp39-cp39-win_amd64.whl (10.6 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 5.1 MB/s eta 0:00:00
# site-packages (from pandas) (2.8.2)
# Requirement already satisfied: pytz>=2020.1 in c:\users\aleyy\anaconda3\lib\site-packa
# Requirement already satisfied: numpy>=1.18.5 in c:\users\aleyy\anaconda3\lib\site-pack
# ages (from pandas) (1.22.3)
# Requirement already satisfied: six>=1.5 in c:\users\aleyy\anaconda3\lib\site-packages
# (from python-dateutil>=2.8.1->pandas) (1.16.0)
# Installing collected packages: pandas
# Successfully installed pandas-1.4.3
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> pip install pandas=1.2.1
# ERROR: Invalid requirement: 'pandas=1.2.1'
# Hint: = is not a valid operator. Did you mean == ?
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> pip install pandas==1.2.1
# Collecting pandas==1.2.1
#   Downloading pandas-1.2.1-cp39-cp39-win_amd64.whl (9.3 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.3/9.3 MB 4.3 MB/s eta 0:00:00
# Requirement already satisfied: pytz>=2017.3 in c:\users\aleyy\anaconda3\lib\site-packa
# ges (from pandas==1.2.1) (2022.1)
# Requirement already satisfied: python-dateutil>=2.7.3 in c:\users\aleyy\anaconda3\lib\
# site-packages (from pandas==1.2.1) (2.8.2)
# ages (from pandas==1.2.1) (1.22.3)
# Requirement already satisfied: six>=1.5 in c:\users\aleyy\anaconda3\lib\site-packages
# (from python-dateutil>=2.7.3->pandas==1.2.1) (1.16.0)
# Installing collected packages: pandas
#   Attempting uninstall: pandas
#     Found existing installation: pandas 1.4.3
#     Uninstalling pandas-1.4.3:
#       Successfully uninstalled pandas-1.4.3
# Successfully installed pandas-1.2.1
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda list
# # packages in environment at C:\Users\aleyy\anaconda3:
# #
# # Name                    Version                   Build  Channel
# _ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
# anaconda-client           1.10.0           py39haa95532_0
# anaconda-navigator        2.1.1                    py39_0
# anyio                     3.5.0            py39haa95532_0
# argon2-cffi               21.3.0             pyhd3eb1b0_0
# argon2-cffi-bindings      21.2.0           py39h2bbff1b_0
# asttokens                 2.0.5              pyhd3eb1b0_0
# attrs                     21.4.0             pyhd3eb1b0_0
# babel                     2.9.1              pyhd3eb1b0_0
# backcall                  0.2.0              pyhd3eb1b0_0
# backports                 1.1                pyhd3eb1b0_0
# backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
# backports.tempfile        1.0                pyhd3eb1b0_1
# backports.weakref         1.0.post1                  py_1
# beautifulsoup4            4.11.1           py39haa95532_0
# blas                      1.0                         mkl
# bleach                    4.1.0              pyhd3eb1b0_0
# brotlipy                  0.7.0           py39h2bbff1b_1003
# bzip2                     1.0.8                he774522_0
# ca-certificates           2022.4.26            haa95532_0
# certifi                   2022.6.15        py39haa95532_0
# cffi                      1.15.0           py39h2bbff1b_1
# chardet                   4.0.0           py39haa95532_1003
# charset-normalizer        2.0.4              pyhd3eb1b0_0
# click                     8.0.4            py39haa95532_0
# clyent                    1.2.2            py39haa95532_1
# colorama                  0.4.4              pyhd3eb1b0_0
# conda                     4.13.0           py39haa95532_0
# conda-build               3.21.9           py39haa95532_0
# conda-content-trust       0.1.1              pyhd3eb1b0_0
# conda-env                 2.6.0                         1
# conda-package-handling    1.8.1            py39h8cc25b3_0
# conda-repo-cli            1.0.4              pyhd3eb1b0_0
# conda-token               0.3.0              pyhd3eb1b0_0
# conda-verify              3.4.2                      py_1
# console_shortcut          0.1.1                         4
# cryptography              3.4.8            py39h71e12ea_0
# debugpy                   1.5.1            py39hd77b12b_0
# decorator                 5.1.1              pyhd3eb1b0_0
# defusedxml                0.7.1              pyhd3eb1b0_0
# entrypoints               0.4              py39haa95532_0
# executing                 0.8.3              pyhd3eb1b0_0
# filelock                  3.6.0              pyhd3eb1b0_0
# freetype                  2.10.4               hd328e21_0
# future                    0.18.2           py39haa95532_1
# glob2                     0.7                pyhd3eb1b0_0
# icu                       58.2                 ha925a31_3
# idna                      3.3                pyhd3eb1b0_0
# intel-openmp              2021.4.0          haa95532_3556
# ipykernel                 6.9.1            py39haa95532_0
# ipython                   8.3.0            py39haa95532_0
# ipython_genutils          0.2.0              pyhd3eb1b0_1
# ipywidgets                7.6.5              pyhd3eb1b0_1
# jedi                      0.18.1           py39haa95532_1
# jinja2                    2.11.3             pyhd3eb1b0_0
# jpeg                      9e                   h2bbff1b_0
# json5                     0.9.6              pyhd3eb1b0_0
# jsonschema                4.4.0            py39haa95532_0
# jupyter_client            7.2.2            py39haa95532_0
# jupyter_core              4.10.0           py39haa95532_0
# jupyter_server            1.17.1           py39haa95532_0
# jupyterlab                3.3.2              pyhd3eb1b0_0
# jupyterlab_pygments       0.1.2                      py_0
# jupyterlab_server         2.10.3             pyhd3eb1b0_1
# jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
# libarchive                3.5.2                h214662b_0
# libiconv                  1.16                 h2bbff1b_2
# liblief                   0.11.5               hd77b12b_1
# libpng                    1.6.37               h2a8f88b_0
# libtiff                   4.2.0                he0120a3_1
# libwebp                   1.2.2                h2bbff1b_0
# libxml2                   2.9.14               h0ad7f3c_0
# lz4-c                     1.9.3                h2bbff1b_1
# markupsafe                2.0.1            py39h2bbff1b_0
# matplotlib-inline         0.1.2              pyhd3eb1b0_2
# menuinst                  1.4.18           py39h59b6b97_0
# mistune                   0.8.4           py39h2bbff1b_1000
# mkl                       2021.4.0           haa95532_640
# mkl-service               2.4.0            py39h2bbff1b_0
# mkl_fft                   1.3.1            py39h277e83a_0
# mkl_random                1.2.2            py39hf11a4ad_0
# navigator-updater         0.2.1            py39haa95532_0
# nbclassic                 0.3.5              pyhd3eb1b0_0
# nbclient                  0.5.13           py39haa95532_0
# nbconvert                 6.4.4            py39haa95532_0
# nbformat                  5.3.0            py39haa95532_0
# nest-asyncio              1.5.5            py39haa95532_0
# notebook                  6.4.11           py39haa95532_0
# numpy                     1.22.3           py39h7a0a035_0
# numpy-base                1.22.3           py39hca35cd5_0
# openssl                   1.1.1p               h2bbff1b_0
# packaging                 21.3               pyhd3eb1b0_0
# pandas                    1.2.1                    pypi_0    pypi
# pandocfilters             1.5.0              pyhd3eb1b0_0
# parso                     0.8.3              pyhd3eb1b0_0
# pickleshare               0.7.5           pyhd3eb1b0_1003
# pillow                    9.0.1            py39hdc2b20a_0
# pip                       21.2.4           py39haa95532_0
# pkginfo                   1.8.2              pyhd3eb1b0_0
# powershell_shortcut       0.0.1                         3
# prometheus_client         0.13.1             pyhd3eb1b0_0
# prompt-toolkit            3.0.20             pyhd3eb1b0_0
# psutil                    5.9.0            py39h2bbff1b_0
# pure_eval                 0.2.2              pyhd3eb1b0_0
# py-lief                   0.11.5           py39hd77b12b_1
# pycosat                   0.6.3            py39h2bbff1b_0
# pycparser                 2.21               pyhd3eb1b0_0
# pygments                  2.11.2             pyhd3eb1b0_0
# pyjwt                     2.1.0            py39haa95532_0
# pyopenssl                 21.0.0             pyhd3eb1b0_1
# pyparsing                 3.0.4              pyhd3eb1b0_0
# pyqt                      5.9.2            py39hd77b12b_6
# pyrsistent                0.18.0           py39h196d8e1_0
# pysocks                   1.7.1            py39haa95532_0
# python                    3.9.7                h6244533_1
# python-dateutil           2.8.2              pyhd3eb1b0_0
# python-fastjsonschema     2.15.1             pyhd3eb1b0_0
# python-libarchive-c       2.9                pyhd3eb1b0_1
# pytz                      2022.1           py39haa95532_0
# pywin32                   302              py39h2bbff1b_2
# pywinpty                  2.0.2            py39h5da7b33_0
# pyyaml                    6.0              py39h2bbff1b_1
# pyzmq                     22.3.0           py39hd77b12b_2
# qt                        5.9.7            vc14h73c81de_0
# qtpy                      2.0.1              pyhd3eb1b0_0
# requests                  2.28.0           py39haa95532_0
# ruamel_yaml               0.15.100         py39h2bbff1b_0
# send2trash                1.8.0              pyhd3eb1b0_1
# setuptools                61.2.0           py39haa95532_0
# sip                       4.19.13          py39hd77b12b_0
# six                       1.16.0             pyhd3eb1b0_1
# sniffio                   1.2.0            py39haa95532_1
# soupsieve                 2.3.1              pyhd3eb1b0_0
# sqlite                    3.38.5               h2bbff1b_0
# stack_data                0.2.0              pyhd3eb1b0_0
# terminado                 0.13.1           py39haa95532_0
# testpath                  0.6.0            py39haa95532_0
# tk                        8.6.12               h2bbff1b_0
# tornado                   6.1              py39h2bbff1b_0
# tqdm                      4.64.0           py39haa95532_0
# traitlets                 5.1.1              pyhd3eb1b0_0
# typing-extensions         4.1.1                hd3eb1b0_0
# typing_extensions         4.1.1              pyh06a4308_0
# tzdata                    2022a                hda174b7_0
# ujson                     5.1.0            py39hd77b12b_0
# urllib3                   1.26.9           py39haa95532_0
# vc                        14.2                 h21ff451_1
# vs2015_runtime            14.27.29016          h5e58377_2
# wcwidth                   0.2.5              pyhd3eb1b0_0
# webencodings              0.5.1            py39haa95532_1
# websocket-client          0.58.0           py39haa95532_4
# win_inet_pton             1.1.0            py39haa95532_0
# wincertstore              0.2              py39haa95532_2
# winpty                    0.4.3                         4
# xmltodict                 0.12.0             pyhd3eb1b0_0
# xz                        5.2.5                h8cc25b3_1
# yaml                      0.2.5                he774522_0
# zlib                      1.2.12               h8cc25b3_2
# zstd                      1.5.2                h19a0ad4_0
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env export > environment.yaml
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> ls
#
#
#     Directory: C:\Users\aleyy\Desktop\miuul-yaz-kampi
#
# d-----         3.07.2022     02:26                .idea
# d-----         3.07.2022     03:06                01_calisma-ortami-ayarlari
# -a----         3.07.2022     03:03          11378 environment.yaml
# -a----         2.07.2022     21:49             69 README.md
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda deactive
#
# CommandNotFoundError: No command 'conda deactive'.
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda deactivate
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env remove -n my_aleyna
# Remove all packages in environment C:\Users\aleyy\anaconda3\envs\my_aleyna:
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda environment list
#
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# base                  *  C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env create -f environment.yaml
# CondaValueError: prefix already exists: C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env create -f environment.yaml
#
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# base                  *  C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda abc create -f environment.yaml
#
# CommandNotFoundError: No command 'conda abc'.
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env create --f environment.yaml
#                                   [-k] [--offline] [--force] [-d]
#                                   [--no-default-packages] [--json] [-v] [-q]
#                                   [--experimental-solver {classic,libmamba,libmamba-dr
# aft}]
# conda-env-script.py create: error: ambiguous option: --f could match --file, --force
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# #
# base                  *  C:\Users\aleyy\anaconda3
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda activate myenv
#
# EnvironmentNameNotFound: Could not find conda environment: myenv
# You can list all discoverable environments with `conda info --envs`.
#
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda list
# # packages in environment at C:\Users\aleyy\anaconda3:
# #
# # Name                    Version                   Build  Channel
# _ipyw_jlab_nb_ext_conf    0.1.0            py39haa95532_0
# anaconda-client           1.10.0           py39haa95532_0
# anaconda-navigator        2.1.1                    py39_0
# anyio                     3.5.0            py39haa95532_0
# argon2-cffi               21.3.0             pyhd3eb1b0_0
# argon2-cffi-bindings      21.2.0           py39h2bbff1b_0
# asttokens                 2.0.5              pyhd3eb1b0_0
# attrs                     21.4.0             pyhd3eb1b0_0
# babel                     2.9.1              pyhd3eb1b0_0
# backcall                  0.2.0              pyhd3eb1b0_0
# backports                 1.1                pyhd3eb1b0_0
# backports.functools_lru_cache 1.6.4              pyhd3eb1b0_0
# backports.tempfile        1.0                pyhd3eb1b0_1
# backports.weakref         1.0.post1                  py_1
# beautifulsoup4            4.11.1           py39haa95532_0
# blas                      1.0                         mkl
# bleach                    4.1.0              pyhd3eb1b0_0
# brotlipy                  0.7.0           py39h2bbff1b_1003
# bzip2                     1.0.8                he774522_0
# ca-certificates           2022.4.26            haa95532_0
# certifi                   2022.6.15        py39haa95532_0
# cffi                      1.15.0           py39h2bbff1b_1
# chardet                   4.0.0           py39haa95532_1003
# charset-normalizer        2.0.4              pyhd3eb1b0_0
# click                     8.0.4            py39haa95532_0
# clyent                    1.2.2            py39haa95532_1
# colorama                  0.4.4              pyhd3eb1b0_0
# conda                     4.13.0           py39haa95532_0
# conda-build               3.21.9           py39haa95532_0
# conda-content-trust       0.1.1              pyhd3eb1b0_0
# conda-env                 2.6.0                         1
# conda-package-handling    1.8.1            py39h8cc25b3_0
# conda-repo-cli            1.0.4              pyhd3eb1b0_0
# conda-token               0.3.0              pyhd3eb1b0_0
# conda-verify              3.4.2                      py_1
# console_shortcut          0.1.1                         4
# cryptography              3.4.8            py39h71e12ea_0
# debugpy                   1.5.1            py39hd77b12b_0
# decorator                 5.1.1              pyhd3eb1b0_0
# defusedxml                0.7.1              pyhd3eb1b0_0
# entrypoints               0.4              py39haa95532_0
# executing                 0.8.3              pyhd3eb1b0_0
# filelock                  3.6.0              pyhd3eb1b0_0
# freetype                  2.10.4               hd328e21_0
# future                    0.18.2           py39haa95532_1
# glob2                     0.7                pyhd3eb1b0_0
# icu                       58.2                 ha925a31_3
# idna                      3.3                pyhd3eb1b0_0
# intel-openmp              2021.4.0          haa95532_3556
# ipykernel                 6.9.1            py39haa95532_0
# ipython                   8.3.0            py39haa95532_0
# ipython_genutils          0.2.0              pyhd3eb1b0_1
# ipywidgets                7.6.5              pyhd3eb1b0_1
# jedi                      0.18.1           py39haa95532_1
# jinja2                    2.11.3             pyhd3eb1b0_0
# jpeg                      9e                   h2bbff1b_0
# json5                     0.9.6              pyhd3eb1b0_0
# jsonschema                4.4.0            py39haa95532_0
# jupyter_client            7.2.2            py39haa95532_0
# jupyter_core              4.10.0           py39haa95532_0
# jupyter_server            1.17.1           py39haa95532_0
# jupyterlab                3.3.2              pyhd3eb1b0_0
# jupyterlab_pygments       0.1.2                      py_0
# jupyterlab_server         2.10.3             pyhd3eb1b0_1
# jupyterlab_widgets        1.0.0              pyhd3eb1b0_1
# libarchive                3.5.2                h214662b_0
# libiconv                  1.16                 h2bbff1b_2
# liblief                   0.11.5               hd77b12b_1
# libpng                    1.6.37               h2a8f88b_0
# libtiff                   4.2.0                he0120a3_1
# libwebp                   1.2.2                h2bbff1b_0
# libxml2                   2.9.14               h0ad7f3c_0
# lz4-c                     1.9.3                h2bbff1b_1
# markupsafe                2.0.1            py39h2bbff1b_0
# matplotlib-inline         0.1.2              pyhd3eb1b0_2
# menuinst                  1.4.18           py39h59b6b97_0
# mistune                   0.8.4           py39h2bbff1b_1000
# mkl                       2021.4.0           haa95532_640
# mkl-service               2.4.0            py39h2bbff1b_0
# mkl_fft                   1.3.1            py39h277e83a_0
# mkl_random                1.2.2            py39hf11a4ad_0
# navigator-updater         0.2.1            py39haa95532_0
# nbclassic                 0.3.5              pyhd3eb1b0_0
# nbclient                  0.5.13           py39haa95532_0
# nbconvert                 6.4.4            py39haa95532_0
# nbformat                  5.3.0            py39haa95532_0
# nest-asyncio              1.5.5            py39haa95532_0
# notebook                  6.4.11           py39haa95532_0
# numpy                     1.22.3           py39h7a0a035_0
# numpy-base                1.22.3           py39hca35cd5_0
# openssl                   1.1.1p               h2bbff1b_0
# packaging                 21.3               pyhd3eb1b0_0
# pandas                    1.2.1                    pypi_0    pypi
# pandocfilters             1.5.0              pyhd3eb1b0_0
# parso                     0.8.3              pyhd3eb1b0_0
# pickleshare               0.7.5           pyhd3eb1b0_1003
# pillow                    9.0.1            py39hdc2b20a_0
# pip                       21.2.4           py39haa95532_0
# pkginfo                   1.8.2              pyhd3eb1b0_0
# powershell_shortcut       0.0.1                         3
# prometheus_client         0.13.1             pyhd3eb1b0_0
# prompt-toolkit            3.0.20             pyhd3eb1b0_0
# psutil                    5.9.0            py39h2bbff1b_0
# pure_eval                 0.2.2              pyhd3eb1b0_0
# py-lief                   0.11.5           py39hd77b12b_1
# pycosat                   0.6.3            py39h2bbff1b_0
# pycparser                 2.21               pyhd3eb1b0_0
# pygments                  2.11.2             pyhd3eb1b0_0
# pyjwt                     2.1.0            py39haa95532_0
# pyopenssl                 21.0.0             pyhd3eb1b0_1
# pyparsing                 3.0.4              pyhd3eb1b0_0
# pyqt                      5.9.2            py39hd77b12b_6
# pyrsistent                0.18.0           py39h196d8e1_0
# pysocks                   1.7.1            py39haa95532_0
# python                    3.9.7                h6244533_1
# python-dateutil           2.8.2              pyhd3eb1b0_0
# python-fastjsonschema     2.15.1             pyhd3eb1b0_0
# python-libarchive-c       2.9                pyhd3eb1b0_1
# pytz                      2022.1           py39haa95532_0
# pywin32                   302              py39h2bbff1b_2
# pywinpty                  2.0.2            py39h5da7b33_0
# pyyaml                    6.0              py39h2bbff1b_1
# pyzmq                     22.3.0           py39hd77b12b_2
# qt                        5.9.7            vc14h73c81de_0
# qtpy                      2.0.1              pyhd3eb1b0_0
# requests                  2.28.0           py39haa95532_0
# ruamel_yaml               0.15.100         py39h2bbff1b_0
# send2trash                1.8.0              pyhd3eb1b0_1
# setuptools                61.2.0           py39haa95532_0
# sip                       4.19.13          py39hd77b12b_0
# six                       1.16.0             pyhd3eb1b0_1
# sniffio                   1.2.0            py39haa95532_1
# soupsieve                 2.3.1              pyhd3eb1b0_0
# sqlite                    3.38.5               h2bbff1b_0
# stack_data                0.2.0              pyhd3eb1b0_0
# terminado                 0.13.1           py39haa95532_0
# testpath                  0.6.0            py39haa95532_0
# tk                        8.6.12               h2bbff1b_0
# tornado                   6.1              py39h2bbff1b_0
# tqdm                      4.64.0           py39haa95532_0
# traitlets                 5.1.1              pyhd3eb1b0_0
# typing-extensions         4.1.1                hd3eb1b0_0
# typing_extensions         4.1.1              pyh06a4308_0
# tzdata                    2022a                hda174b7_0
# ujson                     5.1.0            py39hd77b12b_0
# urllib3                   1.26.9           py39haa95532_0
# vc                        14.2                 h21ff451_1
# vs2015_runtime            14.27.29016          h5e58377_2
# wcwidth                   0.2.5              pyhd3eb1b0_0
# webencodings              0.5.1            py39haa95532_1
# websocket-client          0.58.0           py39haa95532_4
# wheel                     0.37.1             pyhd3eb1b0_0
# widgetsnbextension        3.5.2            py39haa95532_0
# win_inet_pton             1.1.0            py39haa95532_0
# winpty                    0.4.3                         4
# xmltodict                 0.12.0             pyhd3eb1b0_0
# xz                        5.2.5                h8cc25b3_1
# yaml                      0.2.5                he774522_0
# zstd                      1.5.2                h19a0ad4_0
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# #
# base                  *  C:\Users\aleyy\anaconda3
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda create -n myenv
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
#
# ## Package Plan ##
#
#   environment location: C:\Users\aleyy\anaconda3\envs\myenv
#
#
#
# Proceed ([y]/n)? y
#
# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# #
# # To activate this environment, use
# #     $ conda activate myenv
# #
# # To deactivate an active environment, use
# #
# #     $ conda deactivate
# # conda environments:
# #
# base                  *  C:\Users\aleyy\anaconda3
# myenv                    C:\Users\aleyy\anaconda3\envs\myenv
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda env list
# # conda environments:
# #
# base                  *  C:\Users\aleyy\anaconda3
# myenv                    C:\Users\aleyy\anaconda3\envs\myenv
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi> conda activate -n myenv
#
# ArgumentError: activate does not accept more than one argument:
# ['-n', 'myenv']
#
#
# PS C:\Users\aleyy\Desktop\miuul-yaz-kampi>
####