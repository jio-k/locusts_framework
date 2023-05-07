Locusts Framework
Locusts Framework 是一个用于压力测试的框架，用于对接口进行负载测试和压力测试。它提供了灵活和可扩展的方式来模拟大量并发用户，并测量应用的性能和稳定性。

1，安装环境
Python 版本: 3.x
Locust 版本: 2.8.6

2，目录结构
common: 这个目录包含了 Locusts Framework 的核心代码，封装了所有与 Locust 相关的方法和功能。
data: 该目录用于存放测试所需的数据，例如测试数据文件、配置文件等。
report: 在执行压力测试后，生成的测试报告将被存放在该目录中，方便查阅和分享。
scripts: 该目录包含了测试用例的内容，通过编写不同的测试脚本来模拟不同的用户行为和场景。
utils: 这个目录存放了一些辅助工具，可以用来处理测试数据、生成随机数据等。
请确保你已经安装了 Python3 和 Locust 2.8.6 版本，然后按照以下步骤使用 Locusts Framework 进行压力测试：

在 data 目录下准备测试所需的数据文件。
在 scripts 目录下编写测试脚本，定义不同的用户行为和场景。
运行 Locusts Framework，使用命令行或集成工具，指定测试脚本和测试参数进行压力测试。
压力测试结束后，在 report 目录下查看生成的测试报告，分析性能指标和结果。
请参考每个目录下的 README.md 文件，了解更多关于该目录的详细说明和用法。

3，帮助和支持
如果您在使用 Locusts Framework 过程中遇到任何问题或需要帮助，请在 GitHub 上提交 issue，我们将尽快回复并解决问题。

感谢您使用 Locusts Framework 进行压力测试！希望它能帮助您评估和优化您的Web应用的性能。

4，具体case .py的代码解析
4.1 on_test_start 函数：

通过 @events.test_start.add_listener 装饰器指定了一个监听器，在测试开始时触发。
当测试开始时，会打印出 "前置方法启动"。
on_test_stop 函数：

通过 @events.test_stop.add_listener 装饰器指定了一个监听器，在测试结束时触发。
当测试结束时，会打印出 "===测试结束了提示==="。

4.2 Mytask 类：

继承自 MyLocustTask 类。
定义了 on_start 方法，在每个用户启动时调用，会打印出 "用户启动！！！！！"。
定义了 on_stop 方法，在每个用户停止时调用，会打印出 "on_stop"。
定义了 locust_interface_name_pressure_test 方法，作为一个压测接口的测试用例，目前没有具体实现。

4.3 MyCustomShape 类：

继承自 LoadTestShape 类，用于定义负载模式。
定义了 tick 方法，根据不同的运行时间阶段返回不同的用户数和产生率。
QuickstartUser 类：

继承自 FastLocustOperation 类。
定义了 debug_stream 属性，指定了一个日志文件路径。
定义了 wait_time 属性，指定了每个用户执行任务之间的等待时间。
定义了 on_start 方法，在每个用户启动时调用，会打印出 "用户启动！！！！！"。
定义了 on_stop 方法，在每个用户停止时调用，会打印出 "on_stop"。
定义了 tasks 列表，指定了要执行的测试任务。

4.4 if __name__ == '__main__' 部分：
用于指定脚本的入口点。
调用 subprocess.call 方法，执行 locust 命令进行压力测试。
指定了一些 locust 命令的参数，例如使用 --tags 参数指定了要执行的标签，使用 --csv 参数指定了报告的 CSV 输出路径，使用 --headless 参数指定无头模式，使用 --html 参数指定报告的 HTML 输出路径。

4.5 locust自带装饰器补充：
@tag(operation_flow) 装饰器：
这是一个自定义的装饰器函数，被用于给 locust_interface_name_pressure_test 方法打上标签。
operation_flow 是标签的名称，它可以用于在执行 locust 命令时指定要运行的特定测试用例或测试场景。
标签的使用可以帮助你更细粒度地控制要执行的测试用例。

@task 装饰器：
这是 locust 框架提供的装饰器函数，用于将一个方法转换为一个 locust 任务（task）。
locust_interface_name_pressure_test 方法被装饰为一个 locust 任务，表示它是一个要在负载测试中执行的任务。
你可以在这个方法中编写具体的压力测试逻辑，包括发送请求、处理响应等。
这两个装饰器在给定的代码中用于定义和标记压力测试任务。它们是 locust 框架提供的重要功能，用于帮助你组织和执行负载测试。