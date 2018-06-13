### sync
在golang 文档上，golang不希望通过共享内存来进行进程间的协同操作，而是通过channel的方式来进行，当然，golang也提供了共享内存，锁等机制进行协同操作的包；

#### 互斥锁： Mutex 和 RWMutex

 ```go
var m *sync.RWMutex
m = new(sync.RWMutex)
    go m.RLock() 
       // read var
       m.Unlock()
    go m.Lock()
        // write var
       m.Unlock()
```
       
多个goroutine都需要做一个操作，但是这个操作只需要执行一次即可，这就需要Once

```go
var once sync.Once
for i :=0; i<10; i++{
    go func(){
        once.Do(func_val)
    }
}
```
此时多个goroutine只执行一次；

### WaitGroup 和Cond

一个goroutine等待其他多个goroutine执行完毕之后才能继续执行，则这种多协程等待问题需要用WaitGroup
 ```go 
wp := new(sync.WaitGroup)
wp.add(10)
for i:=0; i<10; i++{
    go func(){
        fmt.Println("Done, i=", i)
        wp.Done()
    }()
}
wp.Wait()
 ```
sync.Cond用来控制某个条件下，goroutine进行等待时期，等待信号，然后继续运行：

  ```go
locker := new(sync.Mutex)
cond := sync.NewCond(locker)
done := false
​
cond.L.Lock()
go func(){
    time.Sleep(2e9)
    done = true
    cond.Signal()
}()
​
if (!done){
    cond.Wait()
}
 ```
//sync.BroadCast 用来通知唤醒所有等待的goroutine

```go
var locker = new(sync.Mutex)
var cond = sync.NewCond(locker)
​
func test_function(i int){
    cond.L.Lock()
    cond.Wait()
    fmt.Println("input value:", i)
    cond.L.Unlock()  //需要释放lock
}
​
for i:=0; i<10; i++{
    go test_function(i)
}
cond.BroadCast()
 ```
### 使用channel来实现：【并发请求数据，获取最先返回的那个数据】

```go
func Query(conns []Conn, query string) Result{
    ch := make(chan Result, 1)
    for _, c := range conns{
        go func(c){
            select {
            case ch <- c.DoQuery(query):
            default: //case <- timeout , 另开goroutine，进行time.Sleep(10 * time.Second),即超时
            }
        }(conns)
    }
    return <-ch
}
 ```
 
### sync/atomic 库
sync/atomic库提供了原子 操作的支持，原子操作直接由底层CPU硬件支持；

 ```go 
type Value struct{
    Key string
    Value interface{}
}
​
type Noaway struct{
    Movice atomic.Value
    Total  atomic.Value
}
func NewNoaway()  *Noaway{
    n := new(Noaway)
    n.Movice.Store(&Value{Key: "moive", Val: "Wolf Warrior 2"})
    n.Total.Store("$20000")
    return n
}
​
func main(){
    n := newNoaway()
    val := n.Movies.Load().(*Value)
    total := n.Total.Load().(string)
}
```
