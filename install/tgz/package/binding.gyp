{
  'variables': {
    'openssl_fips': '',
  },
  'targets': [
    {
      'target_name': 'zmq',
      'sources': ['binding.cc'],
      'include_dirs' : ["<!(node -e \"require('nan')\")",'/data/miniconda3/envs/snippet/include'],
      'cflags!': ['-fno-exceptions'],
      'cflags_cc!': ['-fno-exceptions'],
      'libraries': ['/data/miniconda3/envs/snippet/lib/libzmq.so.5.2.4'],
      'cflags_cc': [ '-std=c++17' ]
    }
  ]
}
