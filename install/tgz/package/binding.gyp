{
  'variables': {
    'openssl_fips': '',
  },
  'targets': [
    {
      'target_name': 'zmq',
      'sources': ['binding.cc'],
      'include_dirs' : ["<!(node -e \"require('nan')\")",'/#USERHOME#/miniconda3/envs/js/include'],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'libraries': ['/#USERHOME#/miniconda3/envs/js/lib/libzmq.so.5.2.4'],
      'cflags_cc': [ '-std=c++17' ]
    }
  ]
}
