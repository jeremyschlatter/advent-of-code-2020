-- stack --resolver lts-16.24 script --package "megaparsec relude text"

{-# LANGUAGE NoImplicitPrelude, OverloadedStrings #-}

import Relude
import qualified Data.Text as T
import Text.Megaparsec hiding (many)
import Text.Megaparsec.Char.Lexer

type Row = ((Int, Int), Char, Text)

row :: Parsec Void Text Row
row = do
  lo <- decimal
  skip "-"
  hi <- decimal
  skip " "
  c <- anySingle
  skip ": "
  pw <- takeWhileP empty (/= '\n')
  skip "\n"
  pure ((lo, hi), c, pw)
  where skip = void . chunk

ok :: Row -> Bool
ok ((lo, hi), c, pw) = lo <= n && n <= hi where n = T.count (one c) pw

main :: IO ()
main = do
  readFileText "2.txt" >>=
    either (die . errorBundlePretty) pure . parse (many row) "" >>=
    print . length . filter ok
