'''
Created on Oct 15, 2012

@author: anuvrat
'''

def poker( hands ):
    " Return the best hand: poker([hand,...]) => hand "
    return allmax( hands, key = hand_rank )

def allmax( iterable, key = None ):
    "Return a list of all items equal to the max of the iterable."
    result, maxvalue = [], None
    key = key or ( lambda x : x )

    for x in iterable:
        xval = key( x )
        if not result or xval > maxvalue: result, maxvalue = [x], xval
        elif xval == maxvalue: result.append( x )
    return result

def hand_rank( hand ):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks( hand )
    if straight( ranks ) and flush( hand ): return ( 8, max( ranks ) )
    elif kind( 4, ranks ): return ( 7, kind( 4, ranks ), kind( 1, ranks ) )
    elif kind( 3, ranks ) and kind( 2, ranks ): return ( 6, kind( 3, ranks ), kind( 2, ranks ) )
    elif flush( hand ): return ( 5, ranks )
    elif straight( ranks ): return ( 4, max( ranks ) )
    elif kind( 3, ranks ): return ( 3, kind( 3, ranks ), ranks )
    elif two_pair( ranks ): return ( 2, two_pair( ranks ), ranks )
    elif kind( 2, ranks ): return ( 1, kind( 2, ranks ), ranks )
    else: return ( 0, ranks )

def card_ranks( hand ):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index( r ) for r, s in hand]
    ranks.sort( reverse = True )
    return ranks

def flush( hand ):
    " Return True if all the cards have the same suit "
    suits = [s for r, s in hand]
    return len( set( suits ) ) == 1

def straight( ranks ):
    " Return True if the ordered ranks for a 5-card straight "
    return ( max( ranks ) - min( ranks ) == 4 ) and len( set( ranks ) ) == 5

def kind( n, ranks ):
    """Return the first rank that this hand has exactly n-of-a-kind of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count( r ) == n: return r
    return None

def two_pair( ranks ):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind( 2, ranks )
    lowpair = kind( 2, list( reversed( ranks ) ) )
    if pair and lowpair != pair: return ( pair, lowpair )
    else: return None

winner1 = 0
for line in open( '/Users/anuvrat/git/project-euler-python/resource/problem_54_input.txt', 'r' ):
    cards = line.split()
    h1, h2 = cards[:5], cards[5:]
    if h1 == poker( [h1, h2] )[0]: winner1 += 1

print winner1
