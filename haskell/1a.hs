-- stack --resolver lts-16.24 script

main :: IO ()
main = do
  xs <- fmap read . lines <$> readFile "1.txt"
  print $ head $ [a * b | a <- xs, b <- xs, a + b == 2020]
