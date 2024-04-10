import json

DefaultHTTPStatus = 503;

Status = {
  'MESSAGE' : {
    'Type' : 'String',
    'Default' : 'Service Unavailable'
  }
}

Ping = {
  'MESSAGE' : {
    'Type' : 'String',
    'Default' : 'Service Unavailable'
  }
}

PlaySlots = {
  'MESSAGE' : {
    'Type' : 'String',
    'Default' : 'Service Unavailable'
  },
  'PAYOUT_ID' : {
    'Type' : 'int',
    'Default' : -1
  },
  'PAYOUT' : {
    'Type' : 'double',
    'Default' : -1.0
  },
  'WINNINGS' : {
    'Type' : 'double',
    'Default' : -1.0
  },
}

NewBlackjack = {
  'MESSAGE' : {
    'Type' : 'String',
    'Default' : 'Service Unavailable'
  },
  'PLAYER_SCORE' : {
    'Type' : 'int',
    'Default' : -1
  },
  'PLAYERS_CARDS' : {
    'Type' : 'String',
    'Default' : ''
  },
  'DEALERS_CARDS' : {
    'Type' : 'String',
    'Default' : ''
  },
  'GAME_ENDED' : {
    'Type' : 'boolean',
    'Default' : False
  },
}

UpdateBlackjack = {
  'MESSAGE' : {
    'Type' : 'String',
    'Default' : 'Service Unavailable'
  },
  'GAME_RESULT' : {
    'Type' : 'String',
    'Default' : 'N/A'
  },
  'WINNER' : {
    'Type' : 'String',
    'Default' : 'N/A'
  },
  'PLAYER_SCORE' : {
    'Type' : 'int',
    'Default' : -1
  },
  'DEALER_SCORE' : {
    'Type' : 'int',
    'Default' : -1
  },
  'PAYOUT' : {
    'Type' : 'double',
    'Default' : -1.0
  },
  'GAME_ENDED' : {
    'Type' : 'boolean', 
    'Default' : False
  },
  'PLAYERS_CARDS' : {
    'Type' : 'String', 
    'Default' : ''
  },
  'DEALERS_CARDS' : {
    'Type' : 'String', 
    'Default' : ''
  },
}

LogIn = {
  'MESSAGE' : {
    'Type' : 'String', 
    'Default' : 'Service Unavailable'
  },
  'token' : {
    'Type' : 'String',
    'Default' : 'N/A'
  },
}

CreateUser = {
  'MESSAGE' : {
    'Type' : 'String', 
    'Default' : 'Service Unavailable'
  }
}

Deposit = {
  'MESSAGE' : {
    'Type' : 'String', 
    'Default' : 'Service Unavailable'
  }
}

Withdraw = {
  'MESSAGE' : {
    'Type' : 'String', 
    'Default' : 'Service Unavailable'
  }
}

mappings = {
  'MESSAGE' : {
    'Type' : 'String', 
    'Default' : 'Service Unavailable'
  },
  'Status' : Status,
  'Ping' : Ping,
  'PlaySlots' : PlaySlots,
  'NewBlackjack' : NewBlackjack,
  'UpdateBlackjack' : UpdateBlackjack,
  'LogIn' : LogIn,
  'CreateUser' : CreateUser,
  'Deposit' : Deposit,
  'Withdraw' : Withdraw
}

with open('docs.json', 'w') as outfile:
    json.dump(mappings, outfile)