package com.ssdut.imkg.mapper;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.ssdut.imkg.pojo.Node;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ssdut.imkg.pojo.pub.NodeParam;
import com.ssdut.imkg.pojo.pub.UserRequestParam;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author fanyuanxin
 * @since 2021-04-06
 */
@Component
public interface NodeMapper extends BaseMapper<Node> {

    /**
     * 分页查询节点
     * @param page
     * @param node
     * @return
     */
    IPage<NodeParam> selectNodes(Page<NodeParam> page, @Param("node") NodeParam node);

    /**
     * 获得节点modify username
     * @param id
     * @return
     */
    String getNodeModifyUser(@Param("id")Integer id);

    List<Node> getChildrenNode(@Param("id") Integer id);

    List<Node> getInitNodes();

    List<Node> getParents(@Param("id") Integer id);

    List<String> getNodeName(String name);

    List<String> getAllNodeNames();

    List<Node> searchNodeByName( String name , Integer level);

    List<NodeParam> searchNodeByName2(String name, Integer level);

    IPage<NodeParam> getExpertNodes(Page<NodeParam> page, NodeParam node);

    Integer adoptNode(Integer id,Integer level);

    Integer notAdoptNode(Integer id);
}
