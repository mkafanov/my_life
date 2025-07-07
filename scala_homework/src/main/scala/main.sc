object StringProcessor {
// Убрал функцию processStrings
// и сделал в основном коде преобразования через функции высшего порядкаfilter и map
  def main(args: Array[String]): Unit = {
    val strings = List("apple", "cat", "banana", "dog", "elephant")
    var processedStrings = strings.filter(_.length > 3).map(_.toUpperCase)
    println(s"Processed strings: $processedStrings")
  }
}