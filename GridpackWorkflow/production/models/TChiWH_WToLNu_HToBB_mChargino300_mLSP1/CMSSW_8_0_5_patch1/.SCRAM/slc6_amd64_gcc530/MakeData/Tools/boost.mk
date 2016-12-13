ALL_TOOLS      += boost
boost_EX_INCLUDE := /cvmfs/cms.cern.ch/slc6_amd64_gcc530/external/boost/1.57.0-ikhhed/include
boost_EX_LIB := boost_thread boost_signals boost_date_time
boost_EX_USE := root_cxxdefaults sockets
boost_EX_FLAGS_CPPDEFINES  := -DBOOST_SPIRIT_THREADSAFE -DPHOENIX_THREADSAFE
boost_EX_FLAGS_CXXFLAGS  := -Wno-error=unused-variable

