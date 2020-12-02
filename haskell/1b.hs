-- stack --resolver lts-16.24 script

main :: IO ()
main = do
  xs <- fmap read . lines <$> readFile "1.txt"
  print $ head $ [a * b * c | a <- xs, b <- xs, c <- xs, a + b + c == 2020]
