import hashlib

class SearchableEncryptionScheme:
    """
    基于倒排索引的可搜索加密方案实现
    
    包含以下核心功能：
    1. 加密（encrypt）
    2. 陷门生成（generate_trapdoor）
    3. 文档索引构建（index_document）
    4. 加密检索（search）
    """
    
    def __init__(self):
        """初始化加密索引结构"""
        self.forward_index = {}  # 加密词 -> 原始词集合
        self.inverted_index = {}  # 陷门 -> 加密词集合

    def encrypt(self, word):
        """
        使用SHA-256哈希算法对明文进行加密
        
        Args:
            word (str): 需要加密的明文单词
            
        Returns:
            str: SHA-256加密后的十六进制字符串
        """
        return hashlib.sha256(word.encode()).hexdigest()

    def generate_trapdoor(self, encrypted_word):
        """
        根据加密词生成搜索陷门
        
        Args:
            encrypted_word (str): 已加密的单词
            
        Returns:
            str: 用于检索的陷门值
        """
        return hashlib.sha256(encrypted_word.encode()).hexdigest()

    def index_document(self, document):
        """
        构建加密文档索引
        
        Args:
            document (str): 需要加密索引的文档内容
        """
        print(f"Indexing document: {document}")
        
        for word in document.split():
            encrypted_word = self.encrypt(word)
            trapdoor = self.generate_trapdoor(encrypted_word)

            # 构建正向索引（加密词 -> 原始词）
            if encrypted_word not in self.forward_index:
                self.forward_index[encrypted_word] = set()
            self.forward_index[encrypted_word].add(word)

            # 构建倒排索引（陷门 -> 加密词）
            if trapdoor not in self.inverted_index:
                self.inverted_index[trapdoor] = set()
            self.inverted_index[trapdoor].add(encrypted_word)

    def search(self, query):
        """
        执行加密检索操作
        
        Args:
            query (str): 需要搜索的明文查询词
            
        Returns:
            set: 匹配的原始明文单词集合
        """
        print(f"\nProcessing query: {query}")
        
        encrypted_query = self.encrypt(query)
        trapdoor = self.generate_trapdoor(encrypted_query)
        
        print(f"Generated trapdoor: {trapdoor[:8]}... (first 8 chars shown)")
        
        if trapdoor in self.inverted_index:
            encrypted_results = self.inverted_index[trapdoor]
            results = set()
            
            for encrypted_word in encrypted_results:
                results.update(self.forward_index[encrypted_word])
                
            print(f"Found matching encrypted words: {[e[:8]+'...' for e in encrypted_results]}")
            return results
        else:
            print("No matching trapdoor found in index")
            return set()

if __name__ == "__main__":
    # 初始化加密方案实例
    ses = SearchableEncryptionScheme()
    
    # 待索引的示例文档
    document = "Canon, established in 1937 and headquartered in Tokyo, Japan, is a global leader in imaging and information technology. Renowned for its innovative optical technologies, the company specializes in cameras, printers, medical equipment, and industrial solutions. Guided by the philosophy of symbiosis, Canon aims to create value through technological advancements while contributing to a sustainable society."
    
    # 构建加密索引
    ses.index_document(document)
    
    # 执行搜索查询
    search_query = "Canon"
    search_results = ses.search(search_query)
    
    # 显示最终结果
    print("\nSearch Results:")
    if search_results:
        print(f"匹配查询 '{search_query}' 的结果: {', '.join(search_results)}")
    else:
        print(f"未找到与 '{search_query}' 匹配的结果")